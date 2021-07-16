#File Untuk UI Page Login PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, cafe

class Ui_Login(object):
    def setupUi(self, login):
        login.setObjectName("Login")
        login.resize(439, 582)
        self.widget = QtWidgets.QWidget(login)
        self.widget.setGeometry(QtCore.QRect(20, 10, 401, 541))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(134, 81, 65, 255), stop:1 rgba(139, 139, 139, 255));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(154, 101, 85, 275), stop:1 rgba(159, 159, 159, 275));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:\n"
"    background-color: rgb(198, 184, 174);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 15, 321, 501))
        self.label.setStyleSheet("border-image: url(:/images/kafe 1.jpg);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 15, 321, 501))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.676136 rgba(157, 157, 157, 66), stop:0.6875 rgba(159, 159, 159, 66), stop:1 rgba(124, 124, 124, 92));\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 45, 301, 471))
        self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.LoginTeks = QtWidgets.QLabel(self.widget)
        self.LoginTeks.setGeometry(QtCore.QRect(150, 80, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LoginTeks.setFont(font)
        self.LoginTeks.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.LoginTeks.setObjectName("LoginTeks")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(90, 150, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid rgba(255, 255, 255, 210);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.username.setObjectName("Username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(90, 210, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid rgba(255, 255, 255, 210);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("Password")
        self.loginButton = QtWidgets.QPushButton(self.widget)
        self.loginButton.setGeometry(QtCore.QRect(90, 290, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(178, 34, 34);\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(129, 0, 0);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(129, 0, 0);\n"
"    color: rgb(173, 173, 173);\n"
"    }\n"
"\n"
"")
        self.loginButton.setObjectName("loginButton")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Cafe", "Cafe Membership"))
        self.LoginTeks.setText(_translate("Form", "Log In"))
        self.username.setPlaceholderText(_translate("Form", "Username"))
        self.password.setPlaceholderText(_translate("Form", "Password"))
        self.loginButton.setText(_translate("Form", "L o g  I n"))