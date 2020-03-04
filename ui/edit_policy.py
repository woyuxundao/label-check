# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'l:\label_check\ui\edit_policy.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_policy_dialog(object):
    def setupUi(self, policy_dialog):
        policy_dialog.setObjectName("policy_dialog")
        policy_dialog.resize(822, 618)
        self.verticalLayout = QtWidgets.QVBoxLayout(policy_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(policy_dialog)
        self.widget.setMinimumSize(QtCore.QSize(800, 560))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet("font: 12pt \"楷体\";\n"
"padding-left:20px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.result_t = QtWidgets.QLabel(self.widget)
        self.result_t.setObjectName("result_t")
        self.verticalLayout_2.addWidget(self.result_t)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(policy_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(policy_dialog)
        self.buttonBox.accepted.connect(policy_dialog.accept)
        self.buttonBox.rejected.connect(policy_dialog.reject)
        self.pushButton.clicked.connect(policy_dialog.add_item)
        self.pushButton_2.clicked.connect(policy_dialog.remove_item)
        self.pushButton_4.clicked.connect(policy_dialog.apply_items)
        QtCore.QMetaObject.connectSlotsByName(policy_dialog)

    def retranslateUi(self, policy_dialog):
        _translate = QtCore.QCoreApplication.translate
        policy_dialog.setWindowTitle(_translate("policy_dialog", "编辑规则"))
        self.label.setText(_translate("policy_dialog", "规则名称:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("policy_dialog", "机型"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("policy_dialog", "品名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("policy_dialog", "料号"))
        self.pushButton.setText(_translate("policy_dialog", "添加条目"))
        self.pushButton_2.setText(_translate("policy_dialog", "删除条码"))
        self.pushButton_4.setText(_translate("policy_dialog", "应用"))
        self.result_t.setText(_translate("policy_dialog", "验证结果:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    policy_dialog = QtWidgets.QDialog()
    ui = Ui_policy_dialog()
    ui.setupUi(policy_dialog)
    policy_dialog.show()
    sys.exit(app.exec_())
