from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp ,pyqtSignal,Qt
from ui.login import Ui_Form
from utils import AccountManager

class LoginUI(QWidget,Ui_Form):
    sig_logined = pyqtSignal(str)
    sig_registered = pyqtSignal()
    def __init__(self,parent=None,*arg,**kwargs):
        super().__init__(parent,*arg,**kwargs)
        self.setupUi(self)
        self.setup()
        # self.setAttribute(Qt.WA_DeleteOnClose )

    def setup(self):      
        self.btn_flag = False
        self.account_cb.setFocus()
        validator = QRegExpValidator()
        validator.setRegExp(QRegExp("(\w{6,})"))
        self.passwd_ln.setValidator(validator)

    def regiser_btn(self):
        print("注册按钮被点击")
        self.hide()
        self.sig_registered.emit()

    def qrcode_show(self,):
        if self.btn_flag:
            self.qrcode_btn.resize(40,40)
            self.btn_flag = False
        else:
            self.btn_flag = True
            self.qrcode_btn.resize(120,120)
        # self.qrcode_btn.setStyleSheet("border-image: url(:/fg/resource/qrcode-bg.jpg);width:120px;height:120px;")


    def remenber_passwd(self,chk:bool): 
        print("记住密码被选择",chk)
        pass

    def auto_login(self,chk:bool):
        print("自动登陆已选择",chk)
        pass

    def passwd_validate(self,pd:str) ->bool:
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
        a = AccountManager()#帐号管理类
        if a.validate(user,password):
            # print("验证成功")
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

