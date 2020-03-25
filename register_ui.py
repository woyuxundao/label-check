#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
''' '''
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt ,pyqtSignal
from ui.register import Ui_Form
from utils import AccountManager

class RegisterUI(QWidget,Ui_Form):
    # sig_registered = pyqtSignal(str,str)
    def __init__(self,parent=None,*arg,**kwargs):
        super().__init__(parent,*arg,**kwargs)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)

    def register_info(self):
        user = self.user_ln.text()
        pd1 =self.passwd_re_ln.text()
        pd2 =self.passwd_ln.text()
        if pd1 != pd2 or len(pd1) == 0:
            self.result_ln.setText("两次密码不相符")
            return
        if len(user) <3 or len(pd1) <6:
            self.result_ln.setText("用户名或密码长度不足")
            return
        depart = self.department_cb.currentText()
        job = self.job_cb.currentText()
        email  = self.email_ln.text()
        a = AccountManager()
        if a.add_account((user,pd1,depart,job,email)):
            self.result_ln.setText("注册成功")
            self.clear()        
        else:
            self.result_ln.setText("注册失败,用户名不可重复")
        # print("注册信息")

    def clear(self):
        self.user_ln.clear()
        self.passwd_ln.clear()
        self.passwd_re_ln.clear()
        self.email_ln.clear()

    def exit(self):
        print('退出')
        self.close()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    window = RegisterUI()
    window.show()
    sys.exit(app.exec())
