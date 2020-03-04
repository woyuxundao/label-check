# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'l:\label_check\ui\register.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 600)
        Form.setMaximumSize(QtCore.QSize(550, 600))
        Form.setStyleSheet("")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 60, 341, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.user_ln = QtWidgets.QLineEdit(self.layoutWidget)
        self.user_ln.setStyleSheet("QLineEdit {\n"
"    font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus ,QLineEdit:hover{\n"
"    border:none;\n"
"    border-bottom:1px solid rgb(170, 255, 255);\n"
"}")
        self.user_ln.setClearButtonEnabled(True)
        self.user_ln.setObjectName("user_ln")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.user_ln)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_ln = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_ln.setStyleSheet("QLineEdit {\n"
"    font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus ,QLineEdit:hover{\n"
"    border:none;\n"
"    border-bottom:1px solid rgb(170, 255, 255);\n"
"}")
        self.password_ln.setText("")
        self.password_ln.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_ln.setClearButtonEnabled(True)
        self.password_ln.setObjectName("password_ln")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_ln)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.passwd_re_ln = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwd_re_ln.setStyleSheet("QLineEdit {\n"
"    font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus ,QLineEdit:hover{\n"
"    border:none;\n"
"    border-bottom:1px solid rgb(170, 255, 255);\n"
"}")
        self.passwd_re_ln.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_re_ln.setClearButtonEnabled(True)
        self.passwd_re_ln.setObjectName("passwd_re_ln")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwd_re_ln)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.department_cb = QtWidgets.QComboBox(self.layoutWidget)
        self.department_cb.setStyleSheet("font: 75 11pt \"Arial\";")
        self.department_cb.setObjectName("department_cb")
        self.department_cb.addItem("")
        self.department_cb.addItem("")
        self.department_cb.addItem("")
        self.department_cb.addItem("")
        self.department_cb.addItem("")
        self.department_cb.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.department_cb)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.job_cb = QtWidgets.QComboBox(self.layoutWidget)
        self.job_cb.setStyleSheet("font: 75 11pt \"Arial\";")
        self.job_cb.setObjectName("job_cb")
        self.job_cb.addItem("")
        self.job_cb.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.job_cb)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.result_ln = QtWidgets.QLineEdit(self.layoutWidget)
        self.result_ln.setEnabled(False)
        self.result_ln.setStyleSheet("border:None;\n"
"background-color: transparent;\n"
"color: rgb(0, 0, 255);")
        self.result_ln.setText("")
        self.result_ln.setObjectName("result_ln")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.result_ln)
        self.register_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.register_btn.setStyleSheet("font: 75 11pt \"Arial\";")
        self.register_btn.setObjectName("register_btn")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.register_btn)
        self.exit_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.exit_btn.setStyleSheet("font: 75 11pt \"Arial\";")
        self.exit_btn.setObjectName("exit_btn")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.exit_btn)
        self.email_ln = QtWidgets.QLineEdit(self.layoutWidget)
        self.email_ln.setStyleSheet("QLineEdit {\n"
"    font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus ,QLineEdit:hover{\n"
"    border:none;\n"
"    border-bottom:1px solid rgb(170, 255, 255);\n"
"}")
        self.email_ln.setClearButtonEnabled(True)
        self.email_ln.setObjectName("email_ln")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.email_ln)

        self.retranslateUi(Form)
        self.register_btn.clicked.connect(Form.register_info)
        self.exit_btn.clicked.connect(Form.exit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "用户名:"))
        self.label_2.setText(_translate("Form", "密码:"))
        self.label_3.setText(_translate("Form", "密码确认:"))
        self.label_4.setText(_translate("Form", "部门:"))
        self.department_cb.setItemText(0, _translate("Form", "品管部"))
        self.department_cb.setItemText(1, _translate("Form", "组装部"))
        self.department_cb.setItemText(2, _translate("Form", "金属部"))
        self.department_cb.setItemText(3, _translate("Form", "塑胶部"))
        self.department_cb.setItemText(4, _translate("Form", "行政部"))
        self.department_cb.setItemText(5, _translate("Form", "仓务部"))
        self.label_5.setText(_translate("Form", "职位:"))
        self.job_cb.setItemText(0, _translate("Form", "管理员"))
        self.job_cb.setItemText(1, _translate("Form", "员工"))
        self.label_6.setText(_translate("Form", "邮箱"))
        self.register_btn.setText(_translate("Form", "注册"))
        self.exit_btn.setText(_translate("Form", "退出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
