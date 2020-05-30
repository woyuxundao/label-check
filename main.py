#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
''' '''
import login_ui
import register_ui
import check_ui 

def validate(*widget):
    def tmp(user:str) :
        widget[0].setAccount(user)
        widget[0].show()
        widget[1].hide()   
    return tmp

if __name__ == '__main__':
    import sys
    import os
    #为了实现单例模式
    # filename ="lock"
    # if os.path.exists(filename):
    #     sys.exit()
    # else:
    #     f=open(filename,"w+")
    #     f.close()
    # #为了实现单例模式
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    login_w = login_ui.LoginUI()
    check_w = check_ui.CheckUI()
    register_w = register_ui.RegisterUI()
    login_w.sig_registered.connect(register_w.show)
    login_w.sig_logined.connect(validate(check_w,login_w))
    login_w.show()

    # exit_code =app.exec_()
    # os.remove(filename)
    sys.exit(app.exec_())

