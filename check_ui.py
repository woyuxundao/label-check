#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
__email__ = "huliang168168@sina.com"
__vesion__ ="v0.2a"
''' '''
from typing import List
from PyQt5.QtWidgets import  QMainWindow, QMessageBox,QTableWidgetItem,QTableWidget,QSystemTrayIcon,QAction,QMenu,QWidget,QApplication
from PyQt5.QtGui import QIcon , QColor 
from PyQt5.QtCore import Qt , QDateTime
from ui import Ui_MainWindow
from policy_manager_ui import PolicyManager
from edit_item_ui import EditItem
from checker import Checker
from utils import Log ,Config

class CheckUI(Ui_MainWindow,QMainWindow):
    def __init__(self,parent=None,*arg,**kwargs):
        super().__init__(parent,*arg,**kwargs)
        # self.setAttribute( Qt.WA_SetWindowIcon )
        self.setAttribute(Qt.WA_StyleSheet)
        self.setupUi(self)
        self.chk =None
        self.setup()
        self.input_ln.setFocus()

    def setAccount(self,user:str=None):
        self.user = user if user else "吕健涛"

    def setup(self):
        self.user = None
        #加载日志管理器
        self.log = Log()
        #加载设置器
        self.cfg = Config()
        
        #设置菜单栏的Action,绑定方法
        self.exit_ac.triggered.connect(self.close)
        self.edit_plicy_ac.triggered.connect(self.showPolicyManager)
        self.edit_item_ac.triggered.connect(self.showItemManager)
        self.ab_qt_ac.triggered.connect(lambda _,s="关于qt":QMessageBox.aboutQt(self,s))
        self.ab_author_ac.triggered.connect(self.showAuthor)
        self.ab_version_ac.triggered.connect(self.showVersion)
        self.logout_ac.triggered.connect(self.logout)

        #设置tabelwidgets表头的尺寸#
        self.tableWidget.setColumnWidth(0,140)
        self.tableWidget.setColumnWidth(1,120)
        self.tableWidget.setColumnWidth(2,200)   
        #设置表头的行高
        self.tableWidget.setRowHeight(0,20)
        
        #在客户栏中初始化列表
        self.combo_list=(self.custom_cb,self.module_cb,self.name_cb,self.pn_cb)
        self.custom_cb.addItems(self.cfg.code_data.keys())
        
        #设置系统托盘
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(QIcon(":/bo/resource/ico.png"))
        minimizeAction = QAction("最小化", self, triggered = self.hide)
        maximizeAction = QAction("最大化", self, triggered = self.showMaximized)
        restoreAction = QAction("恢复默认大小", self, triggered = self.showNormal)
        quitAction = QAction("退出", self, triggered = QApplication.instance().quit)  # 退出APP
        self.trayMenu = QMenu(self)
        self.trayMenu.addAction(minimizeAction)
        self.trayMenu.addAction(maximizeAction)
        self.trayMenu.addAction(restoreAction)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(quitAction)
        self.tray.setContextMenu(self.trayMenu)
        self.tray.setToolTip('条码检查标签在这！')
        self.tray.showMessage("条码", '托盘信息内容', icon=1) #icon的值  0没有图标  1是提示  2是警告  3是错误
        self.tray.show()

    def logout(self):
        print(f"用户{self.user}注销登陆:")
        #待实现
    
    def showAuthor(self):
        about_text= f'版权所有 @<b><strong>{__author__}</strong></b> 保留所有权利，本软件产品仅限个人基于个人目的使用,禁止将本软件用于生产、经营等商业用途或其他用途 <br>'+f'作者:{__author__} <br> 邮箱:{__email__}<br>'
        QMessageBox.about(self,"关于作者",about_text)

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
        # evt.ignore()  # 忽略关闭事件
        # self.hide()     # 隐藏窗体

    def check_model_change(self,model:bool):
        # print('校验模式变更:%s'%model)
        status = not model
        for cb in self.combo_list:
            cb.setEnabled(status)

    def changeComboBox(self,combo,txt):
        """改变combobox的信号处理方式"""    
        if combo not in self.combo_list:
            return
        index = self.combo_list.index(combo)
        for cb in self.combo_list[index+1:]:
            cb.blockSignals(True)
            cb.clear()
            cb.blockSignals(False)
        tmp = self.cfg.code_data   
        if index > 0:
            for cb in self.combo_list[:index]:
                tmp = tmp[cb.currentText()]
        if index + 2 < len(self.combo_list):
            self.combo_list[index+1].addItems(tmp[txt].keys()) 
        else:  
            # print("cblist",index+1,len(self.combo_list),tmp[txt])
            self.combo_list[index+1].addItems(tmp[txt])   

    def custom_change(self,txt):
        # print('客户变更:%s'%txt)     
        self.changeComboBox(self.custom_cb,txt)
        #修复客户规格为空时残留上一次数据
      
    def module_change(self,txt):
        # print('机型变更:%s'%txt)
        self.changeComboBox(self.module_cb,txt)

    def name_change(self,txt):
        # print('品名变更:%s'%txt)  
        self.changeComboBox(self.name_cb,txt)   
        
    def input_scan(self, codebar:str):
        # print("扫描的数据:%s"%codebar)
        now = QDateTime.currentDateTime().toString("yyyy-MM-dd HH-mm-ss")
        #设置条码校验器
        if not self.chk:
            self.chk = Checker(self.cfg)

        # print("radio 状态",self.auto_radio.isChecked)
        if not self.auto_radio.isChecked():
            customer ,module ,name ,pn = (i.currentText() for i in self.combo_list)
            #只有combobox有数据时才进行单独的验证
            if len(customer) > 0 and len(pn) >0:           
                self.chk.setMode({"customer":customer,"module":module,"name":name,"pn":pn})
        else:
           self.chk.setMode(None) 
           
        result_b ,result_t =self.chk.check(codebar)
        # print(result_b,result_t)
        if result_b:          
            # print("检查的model：",self.chk.model)
            self.set_combo_text(self.chk.model.values())#校验成功会设置model
            style= "color:blue;"
            result_t  ="PASS"
        else:
            style= "background-color:#FF3030;"
        style += 'font: 11pt "楷体";padding-left:20px;border:none;border-radius:25px;'
        self.result_txt.setStyleSheet(style)
        self.result_txt.setText(result_t+":\n"+codebar)  
        self.write_log(now, result_t, codebar)

    def write_log(self,now,result,codebar):
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
        data = [now, result, codebar, self.user]
        self._addData(self.tableWidget, newrow, data)
        self.log.make(data)

    def _addData(self,w:QTableWidget, row:int ,Data :List[str]):
        font_color = QColor(0,0,0)
        if Data[1] != "PASS":
            font_color = QColor(255,0,0)
        for n,d in enumerate(Data) :
            item =QTableWidgetItem(d)
            # print('正在添加数据', item)
            item.setTextAlignment(Qt.AlignCenter )
            item.setForeground(font_color)
            w.setItem(row ,n ,item)

    def set_combo_text(self,args):
        '''设置QComboBox当前文本，args为所用对应的数值迭代器'''
        for combo ,txt in zip(self.combo_list,args):
            combo.setCurrentText(txt)


if  __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    window = CheckUI()
    window.show()
    sys.exit(app.exec_())