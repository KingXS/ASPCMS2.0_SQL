# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MD5_Decrypt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MD5_Decrypt(object):
    def setupUi(self, MD5_Decrypt):
        MD5_Decrypt.setObjectName("MD5_Decrypt")
        MD5_Decrypt.resize(610, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/PK2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MD5_Decrypt.setWindowIcon(icon)
        self.Before_Decrypt = QtWidgets.QLineEdit(MD5_Decrypt)
        self.Before_Decrypt.setGeometry(QtCore.QRect(220, 60, 321, 31))
        self.Before_Decrypt.setObjectName("Before_Decrypt")
        self.label = QtWidgets.QLabel(MD5_Decrypt)
        self.label.setGeometry(QtCore.QRect(80, 140, 141, 31))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(MD5_Decrypt)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 220, 191, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(MD5_Decrypt)
        self.textEdit.setGeometry(QtCore.QRect(220, 140, 321, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(MD5_Decrypt)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 141, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(MD5_Decrypt)
        QtCore.QMetaObject.connectSlotsByName(MD5_Decrypt)

    def retranslateUi(self, MD5_Decrypt):
        _translate = QtCore.QCoreApplication.translate
        MD5_Decrypt.setWindowTitle(_translate("MD5_Decrypt", "MD5解密"))
        self.label.setText(_translate("MD5_Decrypt", "解密后的值是："))
        self.pushButton_2.setText(_translate("MD5_Decrypt", "开始解密"))
        self.label_2.setText(_translate("MD5_Decrypt", "MD5值是："))

