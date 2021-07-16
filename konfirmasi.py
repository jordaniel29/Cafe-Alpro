#File Untuk UI Page Konfirmasi PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys, os

class Ui_Konfirmasi(object):
    def setupUi(self, konfirmasi):
        konfirmasi.setObjectName("konfirmasi")
        konfirmasi.resize(1000, 700)
        konfirmasi.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(konfirmasi)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1001, 71))
        self.label_2.setStyleSheet(
            "border-color: rgb(170, 0, 0);\n"
            "background-color: rgb(170, 0, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 1001, 71))
        self.label_3.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.CafeTeks = QtWidgets.QLabel(self.centralwidget)
        self.CafeTeks.setGeometry(QtCore.QRect(60, 10, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.CafeTeks.setFont(font)
        self.CafeTeks.setStyleSheet("color:rgb(178, 34, 34);")
        self.CafeTeks.setObjectName("CafeTeks")
        self.btn_signout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signout.setGeometry(QtCore.QRect(830, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.btn_signout.setFont(font)
        self.btn_signout.setStyleSheet(
            "QPushButton {\n"
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
            "    }")
        self.btn_signout.setObjectName("btn_signout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 110, 400, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(178, 34, 34)")
        self.label_4.setObjectName("label_4")
        self.table_daftarmenu = QtWidgets.QTableWidget(
            self.centralwidget)
        self.table_daftarmenu.setGeometry(
            QtCore.QRect(60, 190, 881, 401))
        self.table_daftarmenu.setStyleSheet(
            "background-color:rgb(209, 209, 209);\n"
            "color : rgba(129,0,0,255); \n"
            "border-radius: 20px 20px;")
        self.table_daftarmenu.setObjectName("table_daftarmenu")
        self.table_daftarmenu.setColumnCount(0)
        self.table_daftarmenu.setRowCount(0)
        self.pembatas = QtWidgets.QLabel(self.centralwidget)
        self.pembatas.setGeometry(QtCore.QRect(950, 670, 50, 30))
        self.pembatas.setObjectName("pembatas")
        
        self.labelPesanan = QtWidgets.QLabel(self.centralwidget)
        self.labelPesanan.setGeometry(QtCore.QRect(200, 270, 600, 300))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.labelPesanan.setFont(font)
        self.labelPesanan.setStyleSheet(
            "background-color:rgb(209, 209, 209);\n"
            "color : rgba(129,0,0,255); \n"
            "border-radius: 20px 20px;")
        self.labelPesanan.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelPesanan.setObjectName("labelPesanan")
        self.btn_kembali = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kembali.setGeometry(QtCore.QRect(70, 620, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.btn_kembali.setFont(font)
        self.btn_kembali.setStyleSheet("QPushButton {\n"
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
                                         "    }")
        self.btn_kembali.setObjectName("btn_kembali")
        self.btn_konfirmasi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_konfirmasi.setGeometry(QtCore.QRect(750, 620, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.btn_konfirmasi.setFont(font)
        self.btn_konfirmasi.setStyleSheet("QPushButton {\n"
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
                                        "    }")
        self.btn_konfirmasi.setObjectName("btn_konfirmasi")
        
        self.retranslateUi(konfirmasi)
        QtCore.QMetaObject.connectSlotsByName(konfirmasi)

    def retranslateUi(self, konfirmasi):
        _translate = QtCore.QCoreApplication.translate
        konfirmasi.setWindowTitle(
            _translate("konfirmasi", "Cafe Membership"))
        self.btn_signout.setText(
            _translate(
                "konfirmasi",
                "Sign Out"))
        self.label_4.setText(
            _translate(
                "konfirmasi",
                "Konfirmasi Pesanan"))
        self.CafeTeks.setText(_translate("konfirmasi", "Cafe Membership"))
        self.btn_konfirmasi.setText(_translate("konfirmasi", "Konfirmasi"))
        self.btn_kembali.setText(_translate("konfirmasi", "Kembali"))