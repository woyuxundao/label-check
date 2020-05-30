from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

USER_RE =QRegExp("^[a-zA-Z](\w{3,12})$")
PASSWD_RE =QRegExp("^[a-zA-Z](\w{5,12})$")
EMAIL_RE = QRegExp("^([a-zA-Z\d])(\w|\-)+@[a-zA-Z\d]+\.[a-zA-Z]{2,4}$")

Valid_user = QRegExpValidator(USER_RE)
Valid_passwd = QRegExpValidator(PASSWD_RE)
Valid_email = QRegExpValidator(EMAIL_RE)