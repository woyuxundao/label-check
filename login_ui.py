import os
import json
from PyQt5.QtWidgets import QWidget , QCompleter
from PyQt5.QtCore import pyqtSignal, Qt
from ui import Ui_Login
from utils import AccountManager

class LoginUI(QWidget,Ui_Login):
    sig_logined = pyqtSignal(str)
    sig_registered = pyqtSignal()
    def __init__(self,parent=None,*arg,**kwargs):
        super().__init__(parent,*arg,**kwargs)
        self.setupUi(self)
        self.setup()
        self.setAttribute(Qt.WA_DeleteOnClose )
        

    def setup(self):      
        self.qrcode_btn_flag = False
        self.account_cb.setFocus()
        # self.passwd_ln.setValidator(validator)
        self.remember_list ={}
        if os.path.exists("autologin.cfg"):
            with open("autologin.cfg",'r') as f:
                self.remember_list = json.loads(f.read())
                print("remenber_list:",self.remember_list)

        if len(self.remember_list) >0:
            print("读取是否有自动登陆")
            for key ,value in self.remember_list.items():
                if len(value) == 2:
                    self.login_check(key,value[0])
            wordList = self.remember_list.keys()
            completer = QCompleter(wordList, self)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            self.account_cb.setCompleter(completer)    

    def regiser_btn(self):
        print("注册按钮被点击")
        self.hide()
        self.sig_registered.emit()

    def qrcode_show(self,):
        if self.qrcode_btn_flag:
            x , y = self.qrcode_btn.x(),self.qrcode_btn.y()
            # n_x = x+80
            n_y = y+80
            self.qrcode_btn.move(x,n_y)
            self.qrcode_btn.resize(40,40)
            self.qrcode_btn_flag = False
        else:
            self.qrcode_btn_flag = True
            x , y = self.qrcode_btn.x(),self.qrcode_btn.y()
            # n_x = x-80
            n_y = y-80
            self.qrcode_btn.move(x,n_y)
            self.qrcode_btn.resize(120,120)
        # self.qrcode_btn.setStyleSheet("border-image: url(:/fg/resource/qrcode-bg.jpg);width:120px;height:120px;")

    def passwd_validate(self,pd:str) ->bool:
        #待实现
        return True

    def passwd_change(self):
        user = self.account_cb.currentText()
        password = self.passwd_ln.text()
        # print("user password:",user,password)
        #只有满足条件的规则才可使用按钮
        if len(user) >2 and len(password) >5:
            if self.passwd_validate(password):
                self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)    

    def login(self):
        # print("登陆按钮被点击")
        user = self.account_cb.currentText()
        password = self.passwd_ln.text()
        autoflag= self.autologin_rd.isChecked()
        remflag= self.remenber_rd.isChecked()

        a = AccountManager()#帐号管理类
        if a.validate(user,password,autoflag,remflag):   
            self.sig_logined.emit(user)
        else:
            self.result_lb.setText("验证失败,用户名或密码错误")  
      

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app =QApplication(sys.argv)
    window = LoginUI()
    window.show()
    sys.exit(app.exec())

