#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
__vesion__ ="v0.1a"
''' '''
from typing import List
from PyQt5.QtWidgets import  QMainWindow, QMessageBox,QTableWidgetItem,QTableWidget
from PyQt5.QtGui import QIcon , QColor 
from PyQt5.QtCore import Qt , QDateTime
from ui.check import Ui_MainWindow
from policy_manager_ui import PolicyManager
# from edit_poliy_ui import EditPolicy
from edit_item_ui import EditItem
from checker import Checker
from config import Config
from utils import Log

class CheckUI(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None,*arg,**kwargs):
        super().__init__(parent,*arg,**kwargs)
        # self.setAttribute( Qt.WA_SetWindowIcon )
        self.setupUi(self)
        self.setup()
        self.input_ln.setFocus()

    def setAccount(self,user:str):
        self.user = user

    def setup(self):
        self.user = None
        #加载日志管理器
        self.log = Log()
        #加载设置器
        self.cfg = Config()
        
        #设置菜单栏的Action,绑定方法
        self.exit_ac.triggered.connect(self.close)
        #
        self.edit_plicy_ac.triggered.connect(self.showPolicyManager)
        self.edit_item_ac.triggered.connect(self.showItemManager)
        self.ab_qt_ac.triggered.connect(lambda _,s="关于qt":QMessageBox.aboutQt(self,s))
        self.ab_author_ac.triggered.connect(self.showAuthor)
        self.ab_version_ac.triggered.connect(self.showVersion)
        self.logout_ac.triggered.connect(self.logout)

        #设置tabelwidgets表头的尺寸#
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,120)
        self.tableWidget.setColumnWidth(2,220)
        
        # self.tableWidget.setColumnWidth(3,100)
        #setRowHeight(int row,int height)
        
        #在客户栏中初始化列表
        self.custom_cb.addItems( self.cfg.code_data.keys())
    def logout(self):
        print(f"用户{self.user}注销登陆:")
        #待实现
    

    def showAuthor(self):
        QMessageBox.about(self,"关于作者",f"版权归@<b>{__author__}</b>所有\
            <br><br>Email:hulaing168168@sina.com")
        

    def showVersion(self):
        QMessageBox.about(self,"验证系统版本",f"当前验证系统版本:{__vesion__}")
        

    def showPolicyManager(self):
        e =PolicyManager()
        e.exec()
    
    def showItemManager(self):
        e = EditItem()
        e.exec()

    def closeEvent(self,evt):
        # print("关闭窗口")
        self.log =None
        evt.accept()

    #以下程序销毁函数不能正确执行    
    # def __del__(self):
    #     del self.log


    def check_model_change(self,model:bool):
        # print('校验模式变更:%s'%model)
        status = not model
        self.custom_cb.setEnabled(status)
        self.module_cb.setEnabled(status)
        self.name_cb.setEnabled(status)
        self.pn_cb.setEnabled(status)


    def changeComboBox(self,cb,ncb,txt):
        """改变combobox的信号处理方式"""
        ncb.clear()     
        ncb.addItems( cb.point[txt].keys() )
   


    def custom_change(self,txt):
        # print('客户变更:%s'%txt)     
        self.custom_cb.point = self.cfg.code_data
        self.changeComboBox(self.custom_cb,self.module_cb,txt)
      

    def module_change(self,txt):
        # print('机型变更:%s'%txt)
        self.module_cb.point =self.custom_cb.point[self.custom_cb.currentText()]
        self.changeComboBox(self.module_cb,self.name_cb,txt)



    def name_change(self,txt):
        # print('品名变更:%s'%txt)
        self.name_cb.point = self.module_cb.point[self.module_cb.currentText()]
        self.pn_cb.clear()    
        self.pn_cb.addItems( self.name_cb.point[txt])
        
    # def pn_change(self,txt):
    #     print('料号变更:%s'%txt)
        
    def input_scan(self, codebar:str):
        # print("扫描的数据:%s"%codebar)
        #扫描的时间
        now = QDateTime.currentDateTime().toString("yyyy-MM-dd HH-mm-ss")
        #设置条码校验器
        self.chk = Checker()
        # print("radio 状态",self.auto_radio.isChecked)
        if not self.auto_radio.isChecked():
            customer = self.custom_cb.currentText()
            module = self.module_cb.currentText()
            name = self.name_cb.currentText()
            pn = self.pn_cb.currentText()
            print("pn:",pn)
            #只有combobox有数据时才进行单独的验证
            if len(customer) > 0 and len(pn) >0:           
                self.chk.setMode({"customer":customer,"module":module,"name":name,"pn":pn})

        result_b ,result_t =self.chk.check(codebar)

        if result_b:
            self.custom_change(self.chk.sucess["customer"])
            self.module_change(self.chk.sucess["module"])
            self.name_change(self.chk.sucess["name"])
            self.pn_cb.setCurrentText(self.chk.sucess["module"])

            style= "color:blue;"
            result_t  ="PASS"
        else:
            style= "background-color:red;"
        style += 'font: 16pt "楷体";padding-left:20px;border:none;border-radius:25px;'
        self.result_txt.setStyleSheet(style)
        self.result_txt.setText(result_t+":"+codebar)  
        #在tabelwidget中加入记录    
        rows =self.tableWidget.rowCount()

        # print("表格的数据:" ,self.tableWidget.itemAt(rows,0).text())
        if len(self.tableWidget.itemAt(rows,0).text()) >0:
            newrow = rows 
            self.tableWidget.setRowCount(newrow + 1)
            # self.tableWidget.insertRow(0)
        else:
            newrow = rows -1        
        # print("当前有%s行"%newrow)  
        data = [now, result_t, codebar, self.user]
        self.addData(self.tableWidget, newrow, data)
        # addData(self.tableWidget, 1, data)
        
        self.log.make(data)

    def addData(self,w:QTableWidget, row:int ,Data :List[str]):
        for n,d in enumerate(Data) :
            item =QTableWidgetItem(d)
            # print('正在添加数据', item)
            item.setTextAlignment( Qt.AlignCenter )
            if Data[1] != "PASS":
                item.setForeground(QColor(255,0,0))
            w.setItem(row ,n ,item)

        

if  __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    window = CheckUI()

    window.show()
    sys.exit(app.exec_())