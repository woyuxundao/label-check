#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
''' '''
from PyQt5.QtWidgets import QDialog , QTableWidgetItem ,QComboBox
from ui import  Ui_item_dialog
from utils import config

class EditItem(QDialog,Ui_item_dialog):
    def __init__(self,parent=None,*arg,**kwargs):
        super().__init__(parent,*arg,**kwargs)
        self.setupUi(self) 
        self.cfg = config
        self.setup()   
         
    def setup(self):
        self.label.setText("编辑条目")
        self.policy_cb.addItems(self.cfg.policy_cfg.keys())
        # print("item 添加的item",self.cfg.policy_cfg.keys())
        self.tableWidget.setHorizontalHeaderLabels(("机型",'品名','料号'))
        self.todo = [] 

    def change_policy(self,txt:str):
        policy_name = self.policy_cb.currentText()
        # print(self.cfg.code_data)
        if not self.cfg.code_data.get(policy_name):
            return     
        self._policy_tmp =self.cfg.code_data[policy_name]

        for cb in (self.module_cb,self.name_cb,self.pn_cb):
            cb.blockSignals(True)
            cb.clear()
            cb.blockSignals(False)
        # self.module_cb.clear()
        # self.name_cb.clear()
        # self.pn_cb.clear()
        if len(policy_name) >0:
            self.module_cb.addItems(self._policy_tmp.keys())
    
    def change_module(self,txt:str):
        module_name = self.module_cb.currentText()
        if not self._policy_tmp.get(module_name):
            return
        self._module_tmp = self._policy_tmp[module_name]
        self.name_cb.clear()
        self.pn_cb.clear()
        if len(module_name) >0:
            self.name_cb.addItems(self._module_tmp.keys())


    def change_name(self,txt:str):
        name_name = self.name_cb.currentText()
        if not self._module_tmp.get(name_name):
            return
        self._name_tmp = self._module_tmp[name_name]
        self.pn_cb.clear()
        if len(name_name) >0:
            self.pn_cb.addItems(self._name_tmp) 

    def add_module(self):
        policy_name = self.policy_cb.currentText()
        rows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rows +1)
        self.todo.append(("add",[policy_name]+[(rows,i) for i in range(3)]))
        # print("pn的item",[self.tableWidget.item(rows,i) for i in range(3)] )

    def remove_module(self):
        policy_name = self.policy_cb.currentText()
        module_name = self.module_cb.currentText()
        if len(module_name) > 0:
            self.todo.append(("rm",(policy_name,module_name)))
        self.module_cb.removeItem(self.module_cb.currentIndex())
        self.name_cb.clear()
        self.pn_cb.clear()

    def add_name(self):
        policy_name = self.policy_cb.currentText()
        module_name = self.module_cb.currentText()
        if len(module_name) ==0:
            return
        rows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rows +1)
        self.tableWidget.setItem(rows,0,QTableWidgetItem(module_name))
        self.todo.append(("add",[policy_name]+[(rows,i) for i in range(3)]))


        # self.tableWidget.setItem(rows,1,QTableWidgetItem(module_name))


    def remove_name(self):
        policy_name = self.policy_cb.currentText()
        module_name = self.module_cb.currentText()
        name_name = self.name_cb.currentText()
        if len(name_name)>0:
            self.todo.append(("rm",(policy_name,module_name,name_name)))
        self.name_cb.removeItem(self.name_cb.currentIndex())
        self.pn_cb.clear()

    def add_pn(self):
        policy_name = self.policy_cb.currentText()
        module_name = self.module_cb.currentText()
        name_name = self.name_cb.currentText()
        if len(module_name) ==0 or len(name_name) ==0:
            return
        rows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rows +1)
        self.tableWidget.setItem(rows,0,QTableWidgetItem(module_name))
        self.tableWidget.setItem(rows,1,QTableWidgetItem(name_name))
        #把表格中的位置+规则名称发给todo列表
        self.todo.append(("add",[policy_name]+[(rows,i) for i in range(3)]))
        # print("pn的item",self.tableWidget.item(rows,2) )

    def remove_pn(self):
        policy_name = self.policy_cb.currentText()
        module_name = self.module_cb.currentText()
        name_name = self.name_cb.currentText()
        pn_name = self.pn_cb.currentText()        
        if len(pn_name )>0:
            self.todo.append(("rm",(policy_name,module_name,name_name,pn_name)))
        self.pn_cb.removeItem(self.pn_cb.currentIndex())

    def accept(self):
        self.apply_items()
        self.close()
   
    def apply_items(self):
        for tmp in self.todo:
            if tmp[0] == "rm":
                self.cfg.remove_item(tmp[1])
            if tmp[0] == "add":
                tmp_2 = []#存放处理item后的数据
                # print("tmp:",tmp)
                for i in tmp[1][1:]:
                    item = self.tableWidget.item(*i)
                    if item:
                        n = item.text()
                    else:
                        continue
                    if len(n) ==0 :   #避免QTableWidgtItem未设置时为None
                        continue           
                    tmp_2.append(n)
                if len(tmp_2) != 3:
                    continue
                # print("是否执行")
                self.cfg.add_item(tmp[1][:1] +tmp_2)
        #界面刷新动作
        # self.tableWidget.clear()
        self.todo=[]
        self.tableWidget.setRowCount(0)
        self.change_policy(self.policy_cb.currentText())


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    window = EditItem()
    window.show()
    sys.exit(app.exec())
