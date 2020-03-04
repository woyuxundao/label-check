# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'l:\label_check\ui\edit_item.ui'
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
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.policy_cb = QtWidgets.QComboBox(self.widget)
        self.policy_cb.setStyleSheet("font: 11pt \"Arial\";\n"
"padding-left:20px;")
        self.policy_cb.setObjectName("policy_cb")
        self.horizontalLayout.addWidget(self.policy_cb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.module_cb = QtWidgets.QComboBox(self.widget)
        self.module_cb.setStyleSheet("font: 11pt \"Arial\";\n"
"padding-left:20px;")
        self.module_cb.setObjectName("module_cb")
        self.horizontalLayout_3.addWidget(self.module_cb)
        self.module_add_btn = QtWidgets.QPushButton(self.widget)
        self.module_add_btn.setStyleSheet("border-image: url(:/bg/resource/ad.png);\n"
"width:30px;\n"
"height:30px;")
        self.module_add_btn.setText("")
        self.module_add_btn.setObjectName("module_add_btn")
        self.horizontalLayout_3.addWidget(self.module_add_btn)
        self.module_rm_btn = QtWidgets.QPushButton(self.widget)
        self.module_rm_btn.setStyleSheet("border-image: url(:/bg/resource/rm.png);\n"
"width:30px;\n"
"height:30px;")
        self.module_rm_btn.setText("")
        self.module_rm_btn.setObjectName("module_rm_btn")
        self.horizontalLayout_3.addWidget(self.module_rm_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(4, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.name_cb = QtWidgets.QComboBox(self.widget)
        self.name_cb.setStyleSheet("font: 11pt \"Arial\";\n"
"padding-left:20px;")
        self.name_cb.setObjectName("name_cb")
        self.horizontalLayout_4.addWidget(self.name_cb)
        self.name_add_btn = QtWidgets.QPushButton(self.widget)
        self.name_add_btn.setStyleSheet("border-image: url(:/bg/resource/ad.png);\n"
"width:30px;\n"
"height:30px;")
        self.name_add_btn.setText("")
        self.name_add_btn.setObjectName("name_add_btn")
        self.horizontalLayout_4.addWidget(self.name_add_btn)
        self.name_rm_btn = QtWidgets.QPushButton(self.widget)
        self.name_rm_btn.setStyleSheet("border-image: url(:/bg/resource/rm.png);\n"
"width:30px;\n"
"height:30px;")
        self.name_rm_btn.setText("")
        self.name_rm_btn.setObjectName("name_rm_btn")
        self.horizontalLayout_4.addWidget(self.name_rm_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 3)
        self.horizontalLayout_4.setStretch(4, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.pn_cb = QtWidgets.QComboBox(self.widget)
        self.pn_cb.setStyleSheet("font: 11pt \"Arial\";\n"
"padding-left:20px;")
        self.pn_cb.setObjectName("pn_cb")
        self.horizontalLayout_5.addWidget(self.pn_cb)
        self.pn_add_btn = QtWidgets.QPushButton(self.widget)
        self.pn_add_btn.setStyleSheet("border-image: url(:/bg/resource/ad.png);\n"
"width:30px;\n"
"height:30px;")
        self.pn_add_btn.setText("")
        self.pn_add_btn.setObjectName("pn_add_btn")
        self.horizontalLayout_5.addWidget(self.pn_add_btn)
        self.pn_rm_btn = QtWidgets.QPushButton(self.widget)
        self.pn_rm_btn.setStyleSheet("border-image: url(:/bg/resource/rm.png);\n"
"width:30px;\n"
"height:30px;")
        self.pn_rm_btn.setText("")
        self.pn_rm_btn.setObjectName("pn_rm_btn")
        self.horizontalLayout_5.addWidget(self.pn_rm_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 3)
        self.horizontalLayout_5.setStretch(4, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.apply_btn = QtWidgets.QPushButton(self.widget)
        self.apply_btn.setObjectName("apply_btn")
        self.horizontalLayout_2.addWidget(self.apply_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(policy_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.policy_cb)
        self.label_2.setBuddy(self.module_cb)
        self.label_3.setBuddy(self.name_cb)
        self.label_4.setBuddy(self.pn_cb)

        self.retranslateUi(policy_dialog)
        self.buttonBox.accepted.connect(policy_dialog.accept)
        self.buttonBox.rejected.connect(policy_dialog.reject)
        self.apply_btn.clicked.connect(policy_dialog.apply_items)
        self.policy_cb.currentTextChanged['QString'].connect(policy_dialog.change_policy)
        self.module_cb.activated['QString'].connect(policy_dialog.change_module)
        self.name_cb.activated['QString'].connect(policy_dialog.change_name)
        self.module_add_btn.clicked.connect(policy_dialog.add_module)
        self.module_rm_btn.clicked.connect(policy_dialog.remove_module)
        self.name_add_btn.clicked.connect(policy_dialog.add_name)
        self.name_rm_btn.clicked.connect(policy_dialog.remove_name)
        self.pn_add_btn.clicked.connect(policy_dialog.add_pn)
        self.pn_rm_btn.clicked.connect(policy_dialog.remove_pn)
        QtCore.QMetaObject.connectSlotsByName(policy_dialog)

    def retranslateUi(self, policy_dialog):
        _translate = QtCore.QCoreApplication.translate
        policy_dialog.setWindowTitle(_translate("policy_dialog", "编辑条目"))
        self.label.setText(_translate("policy_dialog", "规则名称:"))
        self.label_2.setText(_translate("policy_dialog", "机型:"))
        self.label_3.setText(_translate("policy_dialog", "品名:"))
        self.label_4.setText(_translate("policy_dialog", "料号:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("policy_dialog", "机型"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("policy_dialog", "品名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("policy_dialog", "料号"))
        self.apply_btn.setText(_translate("policy_dialog", "应用"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    policy_dialog = QtWidgets.QDialog()
    ui = Ui_policy_dialog()
    ui.setupUi(policy_dialog)
    policy_dialog.show()
    sys.exit(app.exec_())
