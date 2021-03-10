#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''帮助界面显示'''
import os
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

imgs =("help_Page1.png","help_Page3.png","help_Page3.png")

class My_label(QLabel):
    def init(self):
        self.setPixmap(QPixmap(":/fg/resource/"+imgs[0]))
        self.sum=0
        self.setScaledContents(True) #图片自适应
        self.setFixedSize(794,1100)

    def  wheelEvent(self,evt):
        x = evt.angleDelta().y()//240
        self.sum += x
        self.setPixmap(QPixmap(":/fg/resource/"+imgs[self.sum%3]))

        
if  __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    import img_rc
    app =QApplication(sys.argv)
    window = My_label()
    window.init()
    window.show()
    sys.exit(app.exec_())
