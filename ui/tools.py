#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
''' '''
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal ,Qt

class MyLineEdit(QLineEdit):
    signal_keyboarded = pyqtSignal(str)
    def keyPressEvent(self,evt):
        if evt.key()== Qt.Key_Enter or evt.key()== Qt.Key_Return :
            if len(self.text()) > 0:
                self.signal_keyboarded.emit(self.text())
                self.blockSignals(True)
                self.setText("")
                self.blockSignals(False)
        else:
            super().keyPressEvent(evt)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    k =MyLineEdit()
    k.signal_keyboarded.connect(lambda x :print("监听的数据:",x))
    k.show()
    sys.exit(app.exec_())
