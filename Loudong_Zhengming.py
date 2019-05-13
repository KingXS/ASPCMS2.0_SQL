# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loudong_Zhengming.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
#定义一个发射标准输出的信号




class Ui_Loudong_Zhengming(object):
    def setupUi(self, Loudong_Zhengming):
        Loudong_Zhengming.setObjectName("Loudong_Zhengming")
        Loudong_Zhengming.resize(690, 657)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/PK2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Loudong_Zhengming.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Loudong_Zhengming)
        self.pushButton.setGeometry(QtCore.QRect(140, 40, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Loudong_Zhengming)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 40, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Loudong_Zhengming)
        self.pushButton_3.setGeometry(QtCore.QRect(142, 140, 391, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(Loudong_Zhengming)
        self.textEdit.setGeometry(QtCore.QRect(40, 180, 621, 451))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Loudong_Zhengming)
        QtCore.QMetaObject.connectSlotsByName(Loudong_Zhengming)





    def retranslateUi(self, Loudong_Zhengming):
        _translate = QtCore.QCoreApplication.translate
        Loudong_Zhengming.setWindowTitle(_translate("Loudong_Zhengming", "漏洞证明与利用"))
        self.pushButton.setText(_translate("Loudong_Zhengming", "请选择URL文件"))
        self.pushButton_2.setText(_translate("Loudong_Zhengming", "请选择结果保存文件"))
        self.pushButton_3.setText(_translate("Loudong_Zhengming", "开始"))






