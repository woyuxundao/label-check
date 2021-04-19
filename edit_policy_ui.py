#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
''' '''
from PyQt5.QtWidgets import QDialog , QTableWidgetItem ,QComboBox
from PyQt5.QtCore import pyqtSignal
from ui import  Ui_policy_dialog
from utils import config
from checker import Policy

class EditPolicy(QDialog,Ui_policy_dialog):
    data_signal =pyqtSignal(str,str,str,bool) #自定义信号用于两个widgets数据传递 
    def __init__(self,parent=None,*arg,**kwargs):
        super().__init__(parent,*arg,**kwargs)
        self.setupUi(self)      
        self.todo_list =[] 
        self.model = None
        self.__rule_src = None
        self.cfg =config   #配置类 
        self.flag = True   #未提交标识
        self.setup()

    def setup(self,model=None,rule=None):
        # print("model",model)
        self.model = model
        self.__rule_src = rule
        if model is None:
            title= "新建规则"          
        else:
            title ="编辑规则"
            self.lineEdit.setText(model)
            self.lineEdit.setEnabled(False) #编辑模式防止被修改规则名称
            rules = rule.split(";")
            # print(f"rules:{rules}")
            for row , i in enumerate(rules) :
                rule_name,j = i.split(":")   
                # print(f"j:{j}")
                if "," in j:
                    index=j.index(',')
                else:
                    continue
                length = j[:index]
                content = j[index+1:]
                # print("条码规则解析：",rule_name,length,content)
                #增加条码，并输入规则
                self.add_item()
                # print("tablewidget",self.tableWidget.item(0,0))
                self.tableWidget.item(row,0).setText(length)
                self.tableWidget.cellWidget(row,1).setCurrentText(rule_name)
                self.tableWidget.item(row,2).setText(content)
        self.setWindowTitle(title)
        self.tableWidget.setHorizontalHeaderLabels(("长度",'规则','规则内容'))

    def add_item(self):
        now_rows = self.tableWidget.rowCount() 
        self.tableWidget.setRowCount(now_rows + 1)
        cb = QComboBox()
        cb.addItems(self.cfg.policy_cate )#限定的几种规则
        self.tableWidget.setItem(now_rows,0,QTableWidgetItem())
        self.tableWidget.setCellWidget(now_rows,1,cb)
        self.tableWidget.setItem(now_rows,2,QTableWidgetItem())
     
    def remove_item(self,n):
        '''删除条目'''
        row = self.tableWidget.currentRow() 
        if row >= 0:   
            self.tableWidget.removeRow(row)

    def accept(self):
        if self.flag:
            self.apply_items()
        self.close()
    
    def apply_items(self):
        apply_flag = True
        rows = self.tableWidget.rowCount()
        policy_name = self.lineEdit.text()
        if rows <0 or len(policy_name)==0:
            return 
        policy =[]
        for n in range(rows):
            length = self.tableWidget.item(n,0).text()
            rule = self.tableWidget.cellWidget(n,1).currentText()
            content = self.tableWidget.item(n,2).text()
            content.replace("？","?")  #放置作业员输入中文字符
            content.replace("，",",")  #放置作业员输入中文字符
            content.replace("|","|")  #放置作业员输入中文字符
            policy.append(rule + ":" +length +',' + content)
            # print("policy:",";".join(policy))
        try:
            p = Policy(policy_name,';'.join(policy))
        except Exception as e:
            print("规则创建异常",e)
            apply_flag = False
        
        #检查配置是否存在数据,新增模式相同的规则名不可添加,编辑模式都可
        self.data_signal.emit(policy_name,self.__rule_src,";".join(policy),bool(self.model))

        #校验成功
        if apply_flag and  self.flag:
            result_text ="校验结果:成功"
            result_style ="color:blue;"     
            self.flag = False
        #校验失败
        else:
            result_text ="校验结果:失败"
            result_style ="color:red;"
        self.result_t.setText( result_text)
        self.result_t.setStyleSheet(result_style)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    window = EditPolicy()
    window.show()
    sys.exit(app.exec())
