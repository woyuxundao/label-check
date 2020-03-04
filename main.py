#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
''' '''
import login_ui
import register_ui
import check_ui 
from utils import AccountManager

def validate(widget):
    a = AccountManager()
    def tmp(user:str , password:str) ->bool:
        # print("正则核验")
        if a.validate(user,password):
            # print("验证成功")
            widget.setAccount(user)
            widget.show()
    return tmp

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    login_w = login_ui.LoginUI()
    check_w = check_ui.CheckUI()
    register_w = register_ui.RegisterUI()
    login_w.sig_registered.connect(register_w.show)
    login_w.sig_logined.connect(validate(check_w))

    login_w.show()
    sys.exit(app.exec())
