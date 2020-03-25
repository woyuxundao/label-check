# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'l:\label_check\ui\login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 520)
        Form.setMinimumSize(QtCore.QSize(640, 520))
        Form.setMaximumSize(QtCore.QSize(640, 520))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setStyleSheet("border-image: url(:/bg/resource/login.png);")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy)
        self.register_btn.setMinimumSize(QtCore.QSize(120, 40))
        self.register_btn.setStyleSheet("QPushButton {\n"
"    border:1px solid rgb(202, 202, 202);\n"
"    border-radius:20px;\n"
"}")
        self.register_btn.setFlat(True)
        self.register_btn.setObjectName("register_btn")
        self.horizontalLayout.addWidget(self.register_btn, 0, QtCore.Qt.AlignBottom)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(20, 15, 20, 15)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.account_cb = QtWidgets.QComboBox(self.widget_2)
        self.account_cb.setMinimumSize(QtCore.QSize(0, 30))
        self.account_cb.setStyleSheet("QComboBox {\n"
"    border:none;\n"
"    border-bottom:1px solid rgb(7, 7, 7);\n"
"    \n"
"    font: 75 12pt \"Arial\";\n"
"}\n"
"QComboBox:hover{\n"
"    border-bottom: 1px solid rgb(85, 255, 127);\n"
"}\n"
"QComboBox:drop-down{\n"
"    background:transparent;\n"
"}")
        self.account_cb.setEditable(True)
        self.account_cb.setObjectName("account_cb")
        self.gridLayout.addWidget(self.account_cb, 0, 1, 1, 2)
        self.passwd_ln = QtWidgets.QLineEdit(self.widget_2)
        self.passwd_ln.setMinimumSize(QtCore.QSize(0, 30))
        self.passwd_ln.setStyleSheet("QLineEdit {\n"
"    border-style:none;    \n"
"    border-bottom:1px solid rgb(0, 0, 0);    \n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom:1px solid rgb(150, 254, 69);    \n"
"}")
        self.passwd_ln.setText("")
        self.passwd_ln.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_ln.setObjectName("passwd_ln")
        self.gridLayout.addWidget(self.passwd_ln, 1, 1, 1, 2)
        self.autologin_rd = QtWidgets.QRadioButton(self.widget_2)
        self.autologin_rd.setObjectName("autologin_rd")
        self.gridLayout.addWidget(self.autologin_rd, 2, 0, 1, 2)
        self.login_btn = QtWidgets.QPushButton(self.widget_2)
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.login_btn.setStyleSheet("QPushButton {    \n"
"    font: 25 14pt \"等线 Light\";    \n"
"    border-radius:25px;    \n"
"    background-color:rgb(166, 255, 208);\n"
"}\n"
"QPushButton:disabled {    \n"
"    background-color:rgb(195, 195, 195);\n"
"        \n"
"}")
        self.login_btn.setFlat(False)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 4, 0, 1, 3)
        self.result_lb = QtWidgets.QLineEdit(self.widget_2)
        self.result_lb.setEnabled(False)
        self.result_lb.setMinimumSize(QtCore.QSize(0, 30))
        self.result_lb.setStyleSheet("border-style:none;\n"
"font: 9pt \"黑体\";\n"
"background-color: transparent;\n"
"color: rgb(255, 0, 0);")
        self.result_lb.setText("")
        self.result_lb.setObjectName("result_lb")
        self.gridLayout.addWidget(self.result_lb, 3, 0, 1, 3)
        self.remenber_rd = QtWidgets.QRadioButton(self.widget_2)
        self.remenber_rd.setMinimumSize(QtCore.QSize(0, 30))
        self.remenber_rd.setCheckable(True)
        self.remenber_rd.setChecked(False)
        self.remenber_rd.setObjectName("remenber_rd")
        self.gridLayout.addWidget(self.remenber_rd, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.qrcode_btn = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qrcode_btn.sizePolicy().hasHeightForWidth())
        self.qrcode_btn.setSizePolicy(sizePolicy)
        self.qrcode_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.qrcode_btn.setMaximumSize(QtCore.QSize(120, 119))
        self.qrcode_btn.setSizeIncrement(QtCore.QSize(0, 0))
        self.qrcode_btn.setStyleSheet("border-image: url(:/fg/resource/qrcode-bg.jpg);")
        self.qrcode_btn.setText("")
        self.qrcode_btn.setObjectName("qrcode_btn")
        self.verticalLayout_2.addWidget(self.qrcode_btn, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.widget_4)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 5)
        self.label_2.setBuddy(self.account_cb)
        self.label_3.setBuddy(self.passwd_ln)

        self.retranslateUi(Form)
        self.register_btn.clicked.connect(Form.regiser_btn)
        self.qrcode_btn.clicked.connect(Form.qrcode_show)
        self.passwd_ln.textChanged['QString'].connect(Form.passwd_change)
        self.login_btn.clicked.connect(Form.login)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登陆界面"))
        self.register_btn.setText(_translate("Form", "注册"))
        self.label_2.setText(_translate("Form", "用户名:"))
        self.passwd_ln.setToolTip(_translate("Form", "必须包含字母和数字,长度不小于6位"))
        self.passwd_ln.setPlaceholderText(_translate("Form", "必须包含字母和数字"))
        self.autologin_rd.setText(_translate("Form", "自动登陆"))
        self.login_btn.setText(_translate("Form", "登陆"))
        self.login_btn.setShortcut(_translate("Form", "Enter"))
        self.remenber_rd.setText(_translate("Form", "记住密码"))
        self.label_3.setText(_translate("Form", "密码:"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
