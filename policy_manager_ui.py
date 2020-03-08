#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''对条码规则进行编辑的窗口控件'''

from PyQt5.QtWidgets import QDialog ,QTableWidgetItem
from ui.policy_manager import Ui_Dialog
from edit_policy_ui import EditPolicy
from utils import Config


class PolicyManager(QDialog,Ui_Dialog):
    def __init__(self,parent=None,*arg,**kwargs):
        super().__init__(parent,*arg,**kwargs)
        self.setupUi(self)
        #把已设置的信息的函数暂时存储,待最后决定是否保存
        self.todo_list ={"add":[],"remove":[]}#元素按照(函数,"")格式保存
        
    def setConfig(self,config):
        self.cfg = config   #配置类 
        self.setup()       

    def setup(self):      
        policy_len = len(self.cfg.policy_cfg.keys())
        if policy_len == 0:
            return
        self.tableWidget.setRowCount(policy_len)
        #按对应的表格填入数据
        for kv ,row in zip(self.cfg.policy_cfg.items(),range(policy_len)):
            self.tableWidget.setItem(row , 0, QTableWidgetItem(kv[0]))
            self.tableWidget.setItem(row , 1, QTableWidgetItem(kv[1]))

    def todo(self):
        """待办事项"""
        for i in self.todo_list["remove"]:
            self.cfg.remove_policy(i)
        for i in self.todo_list["add"]:
            self.cfg.add_policy(i)
            

    def accept(self):
        #  print("保存已进行的操作,然后退出")
         self.todo()
         super().accept()

    def new_policy(self):
        # print("创建一个新的窗口创建规则")      
        policy_w = EditPolicy() 
        policy_w.setConfig(self.cfg)
        # print(self.policy_w.__dict__)
        policy_w.exec()#QDialog类可行的模态窗口
        self.setup()

    def edit_policy(self):
        # print("创建一个新的窗口编辑规则")
        row = self.tableWidget.currentRow()
        if row < 0:
            return
        txt = self.tableWidget.item(row,0).text()
        # print("row txt",row,txt)
        policy_w = EditPolicy() 
        policy_w.setConfig(self.cfg)
        policy_w.setup(txt)
        policy_w.exec()
        self.setup()


    def del_policy(self):
        row = self.tableWidget.currentRow() 
        # print("当前选择删除选定的行:",row)
        if row >= 0:   
            config_key = self.tableWidget.item(row,0).text()
            # print("config_key",config_key)
            self.tableWidget.removeRow(row)
            self.todo_list["remove"].append(config_key)
            
    
            
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    window = PolicyManager()
    window.show()
    sys.exit(app.exec())
