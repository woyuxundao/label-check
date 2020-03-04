#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
''' '''
from PyQt5.QtWidgets import QDialog , QTableWidgetItem ,QComboBox
from ui.edit_policy import  Ui_policy_dialog
from config import Config
from checker import Policy

class EditPolicy(QDialog,Ui_policy_dialog):
    def __init__(self,parent=None,*arg,**kwargs):
        super().__init__(parent,*arg,**kwargs)
        self.setupUi(self)      
        self.todo_list =[] 
        self.cfg =Config()#配置类

    def setup(self,model=None):
        # print("model",model)
        if model is None:
            title= "新建规则"          
        else:
            title ="编辑规则"
            self.lineEdit.setText(model)
        self.setWindowTitle(title)
        self.tableWidget.setHorizontalHeaderLabels(("长度",'规则','规则内容'))

    def add_item(self,k):
        now_rows = self.tableWidget.rowCount() 
        self.tableWidget.setRowCount(now_rows + 1)
        cb = QComboBox()
        cb.addItems(self.cfg.policy_cate )
        self.tableWidget.setCellWidget(now_rows,1,cb)
        
        

    def remove_item(self,n):
        '''删除条目'''
        row = self.tableWidget.currentRow() 
        # print(self.tableWidget.cellWidget(0,1).currentText())
        # print("当前选择删除选定的行:",row)
        if row >= 0:   
            self.tableWidget.removeRow(row)

    def accept(self):
        for i in self.todo_list:
            self.cfg.edit_policy(*i)
 
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
            policy.append(rule + ":" +length +',' + content)
            # print("policy:",";".join(policy))
        try:
            p = Policy(policy_name,';'.join(policy))
        except Exception as e:
            print("异常",e)
            apply_flag = False

        #校验成功
        if apply_flag:
            self.todo_list.append((policy_name,';'.join(policy)))
            result_text ="校验结果:成功"
            result_style ="color:blue;"
     
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