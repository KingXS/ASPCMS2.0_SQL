# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'URL_caiji.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_URL_caiji(object):
    def setupUi(self, URL_caiji):
        URL_caiji.setObjectName("URL_caiji")
        URL_caiji.resize(513, 311)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/PK2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        URL_caiji.setWindowIcon(icon)
        self.lineEdit = QtWidgets.QLineEdit(URL_caiji)
        self.lineEdit.setGeometry(QtCore.QRect(200, 60, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(URL_caiji)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 130, 341, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(URL_caiji)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 210, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(URL_caiji)
        self.label.setGeometry(QtCore.QRect(70, 70, 111, 20))
        self.label.setStyleSheet("\n"
"font: 10pt \"Agency FB\";")
        self.label.setObjectName("label")

        self.retranslateUi(URL_caiji)
        QtCore.QMetaObject.connectSlotsByName(URL_caiji)

    def retranslateUi(self, URL_caiji):
        _translate = QtCore.QCoreApplication.translate
        URL_caiji.setWindowTitle(_translate("URL_caiji", "URL采集"))
        self.pushButton_2.setText(_translate("URL_caiji", "选择URL保存路径"))
        self.pushButton_3.setText(_translate("URL_caiji", "开始采集"))
        self.label.setText(_translate("URL_caiji", "请输入关键字："))

