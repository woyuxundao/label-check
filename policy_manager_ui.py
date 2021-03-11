#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''对条码规则进行编辑的窗口控件'''

from PyQt5.QtWidgets import QDialog ,QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from ui import Ui_policy_manager
from edit_policy_ui import EditPolicy
from utils import config

class PolicyManager(QDialog,Ui_policy_manager):
    data_update_signal = pyqtSignal()  #向父级窗口通报改更新数据了
    def __init__(self,parent=None,*arg,**kwargs):
        super().__init__(parent,*arg,**kwargs)
        self.setupUi(self)
        #把已设置的信息的函数暂时存储,待最后决定是否保存
        self.todo_list ={"add":[],"remove":[]}     #元素按照(函数,"")格式保存
        self.cfg = config  #配置类 
        self.setup()       

    def setup(self):      
        policy_len = sum(len(i) for i in self.cfg.policy_cfg.values()) #实际规则的长度
        if policy_len == 0:
            return
        self.tableWidget.setRowCount(policy_len) 

        row = 0
        for policy_name , rule_list in self.cfg.policy_cfg.items():
            for rule in rule_list:
                if len(rule)==0 :continue #空内容跳过
                self.tableWidget.setItem(row , 0, QTableWidgetItem(policy_name))
                self.tableWidget.setItem(row , 1, QTableWidgetItem(rule))  
                row += 1              

    def add_src(self,*list):
        '''按照list列表的标志，修改或新增规则'''
        policy_name,rule_s,rule_n,flag = list
        rows = self.tableWidget.rowCount()
        if flag:
            for row in range(rows):
                policy_n = self.tableWidget.item(row,0).text()
                if policy_n != policy_name:
                    continue
                rule = self.tableWidget.item(row,1).text()    
                if rule_s == rule:
                    self.tableWidget.item(row,1).setText(rule_n)         
        else:
            self.tableWidget.setRowCount(rows+1)
            self.tableWidget.setItem(rows , 0, QTableWidgetItem(policy_name))
            self.tableWidget.setItem(rows , 1, QTableWidgetItem(rule_n))    


    def accept(self):
        #  print("保存已进行的操作,然后退出")
        rows = self.tableWidget.rowCount()
        policys ={}
        for row in range(rows):
            policy_name = self.tableWidget.item(row,0).text()
            rule = self.tableWidget.item(row,1).text()     
            policys.setdefault(policy_name,[]).append(rule)
        self.cfg.policy_cfg =policys #更新规则信息
        self.data_update_signal.emit()
        super().accept()

    def new_policy(self):
        # print("创建一个新的窗口创建规则")      
        policy_w = EditPolicy() 
        policy_w.data_signal.connect(self.add_src)
        policy_w.exec()  #QDialog类可行的模态窗口

    def edit_policy(self):
        # print("创建一个新的窗口编辑规则")
        row = self.tableWidget.currentRow()
        if row < 0:
            return
        txt = self.tableWidget.item(row,0).text()#规则名称
        rule = self.tableWidget.item(row,1).text()#规则内容
        print("规则,内容:",txt,rule)
        policy_w = EditPolicy() 
        policy_w.setup(txt,rule)
        policy_w.data_signal.connect(self.add_src)
        policy_w.exec()


    def del_policy(self):
        row = self.tableWidget.currentRow() 
        if row >= 0:   
            self.tableWidget.removeRow(row)

            
    
            
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    window = PolicyManager()
    window.show()
    sys.exit(app.exec())
