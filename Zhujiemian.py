# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Zhujiemian.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Zhu_jiemian(object):
    def setupUi(self, Zhu_jiemian):
        Zhu_jiemian.setObjectName("Zhu_jiemian")
        Zhu_jiemian.resize(988, 675)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/23584/Pictures/lovewallpaper/PK2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Zhu_jiemian.setWindowIcon(icon)
        Zhu_jiemian.setStyleSheet("")
        self.url_collect_button = QtWidgets.QPushButton(Zhu_jiemian)
        self.url_collect_button.setGeometry(QtCore.QRect(170, 337, 101, 131))
        self.url_collect_button.setStyleSheet("font: 12pt \"黑体\";\n"
"color:rgb(0, 85, 255)")
        self.url_collect_button.setObjectName("url_collect_button")
        self.label = QtWidgets.QLabel(Zhu_jiemian)
        self.label.setGeometry(QtCore.QRect(240, 140, 72, 15))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Zhu_jiemian)
        self.label_2.setGeometry(QtCore.QRect(290, 80, 511, 61))
        self.label_2.setStyleSheet("font: 28pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.aspcms_button = QtWidgets.QPushButton(Zhu_jiemian)
        self.aspcms_button.setGeometry(QtCore.QRect(440, 340, 101, 131))
        self.aspcms_button.setStyleSheet("font: 12pt \"黑体\";\n"
"color:rgb(0, 85, 255)")
        self.aspcms_button.setObjectName("aspcms_button")
        self.md5_button = QtWidgets.QPushButton(Zhu_jiemian)
        self.md5_button.setGeometry(QtCore.QRect(680, 340, 101, 131))
        self.md5_button.setStyleSheet("font: 12pt \"黑体\";\n"
"color:rgb(0, 85, 255)")
        self.md5_button.setObjectName("md5_button")
        self.label_3 = QtWidgets.QLabel(Zhu_jiemian)
        self.label_3.setGeometry(QtCore.QRect(210, 540, 511, 20))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Zhu_jiemian)
        self.pushButton.setGeometry(QtCore.QRect(330, 200, 331, 61))
        self.pushButton.setStyleSheet("font: 12pt \"黑体\";\n"
"color:rgb(0, 85, 255)")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Zhu_jiemian)
        self.label_4.setGeometry(QtCore.QRect(350, 580, 541, 41))
        self.label_4.setStyleSheet("\n"
"font: 12pt \"Bell MT\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Zhu_jiemian)
        self.label_5.setGeometry(QtCore.QRect(280, 540, 461, 20))
        self.label_5.setStyleSheet("color:rgb(255, 85, 0);")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Zhu_jiemian)
        QtCore.QMetaObject.connectSlotsByName(Zhu_jiemian)

    def retranslateUi(self, Zhu_jiemian):
        _translate = QtCore.QCoreApplication.translate
        Zhu_jiemian.setWindowTitle(_translate("Zhu_jiemian", "信息安全大课设"))
        self.url_collect_button.setText(_translate("Zhu_jiemian", "URL采集"))
        self.label_2.setText(_translate("Zhu_jiemian", "ASPCMS漏洞检测系统"))
        self.aspcms_button.setText(_translate("Zhu_jiemian", "漏洞证明"))
        self.md5_button.setText(_translate("Zhu_jiemian", "MD5解密"))
        self.pushButton.setText(_translate("Zhu_jiemian", "系统以及分工简介"))
        self.label_4.setText(_translate("Zhu_jiemian", "Copyright © 2018. All rights reserved. "))
        self.label_5.setText(_translate("Zhu_jiemian", "本系统只用于合法检测，请勿用于违法行为，否则自行承担法律责任"))

