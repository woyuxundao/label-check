from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegEx

validator_passwd = QRegExpValidator()
validator_passwd.setRegExp(QRegExp("(\w{6,12})"))