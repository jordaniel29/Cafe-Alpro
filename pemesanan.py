#File Untuk UI Page Pemesanan PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys, os

class Ui_Pemesanan(object):
    def setupUi(self, pemesanan):
        pemesanan.setObjectName("pemesanan")
        pemesanan.resize(1000, 700)
        pemesanan.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(pemesanan)
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
        self.label_4.setGeometry(QtCore.QRect(400, 110, 200, 31))
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
        self.txt_id = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_id.setGeometry(QtCore.QRect(160, 620, 81, 41))
        self.txt_id.setObjectName("txt_id")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 620, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(178, 34, 34)")
        self.label_5.setObjectName("label_5")
        self.btn_pesan = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pesan.setGeometry(QtCore.QRect(250, 620, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.btn_pesan.setFont(font)
        self.btn_pesan.setStyleSheet(
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
        self.btn_pesan.setObjectName("btn_pesan")
        self.btn_hapus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hapus.setGeometry(QtCore.QRect(350, 620, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.btn_hapus.setFont(font)
        self.btn_hapus.setStyleSheet(
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
        self.btn_hapus.setObjectName("btn_hapus")
        self.pembatas = QtWidgets.QLabel(self.centralwidget)
        self.pembatas.setGeometry(QtCore.QRect(950, 670, 50, 30))
        self.pembatas.setObjectName("pembatas")

        self.table_daftarmenu.setAlternatingRowColors(True)
        self.table_daftarmenu.setColumnCount(5)
        self.table_daftarmenu.horizontalHeader().setCascadingSectionResizes(False)
        self.table_daftarmenu.horizontalHeader().setSortIndicatorShown(False)
        self.table_daftarmenu.setColumnWidth(1,300)
        self.table_daftarmenu.setColumnWidth(2,200)
        self.table_daftarmenu.horizontalHeader().setStretchLastSection(True)
        self.table_daftarmenu.verticalHeader().setVisible(False)
        self.table_daftarmenu.verticalHeader().setCascadingSectionResizes(False)
        self.table_daftarmenu.verticalHeader().setStretchLastSection(False)
        self.table_daftarmenu.setHorizontalHeaderLabels(
            ("No Menu",
             "Nama",
             "Harga",
             "Jumlah Tersedia",
             "Jumlah Dipesan"))
        self.btn_selanjutnya = QtWidgets.QPushButton(self.centralwidget)
        self.btn_selanjutnya.setGeometry(QtCore.QRect(750, 620, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.btn_selanjutnya.setFont(font)
        self.btn_selanjutnya.setStyleSheet("QPushButton {\n"
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
        self.btn_selanjutnya.setObjectName("selanjutnyaButton")
        
        self.retranslateUi(pemesanan)
        QtCore.QMetaObject.connectSlotsByName(pemesanan)

    def retranslateUi(self, pemesanan):
        _translate = QtCore.QCoreApplication.translate
        pemesanan.setWindowTitle(
            _translate("pemesanan", "Cafe Membership"))
        self.btn_signout.setText(
            _translate(
                "pemesanan",
                "Sign Out"))
        self.CafeTeks.setText(_translate("konfirmasi", "Cafe Membership"))
        self.label_4.setText(
            _translate(
                "pemesanan",
                "Pemesanan"))
        self.label_5.setText(_translate("pemesanan", "No Menu"))
        self.btn_pesan.setText(_translate("pemesanan", "Pesan"))
        self.btn_hapus.setText(_translate("pemesanan", "Hapus"))
        self.btn_selanjutnya.setText(_translate("pemesanan", "Selanjutnya"))

    