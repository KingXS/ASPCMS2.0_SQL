
#引用各个界面模块
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Zhujiemian import Ui_Zhu_jiemian
from Loudong_Zhengming import Ui_Loudong_Zhengming
from MD5_Decrypt import Ui_MD5_Decrypt
from URL_caiji import Ui_URL_caiji
from Xitong_fengong import Ui_widget

##################################################################################################################################

#引用URL采集函数
from URL_Collect_ThreadPool import main
#引用漏洞证明函数
from ASPCMS_exp import ASPCMS_EXP
#引用MD5解密函数
from MD5 import MD5_

#################################################################################################################################

#应用的系统模块

import requests
from bs4 import BeautifulSoup as bs   #将模块重命名
import re
from concurrent.futures import ThreadPoolExecutor,wait
import sys


#############################################################################################################################


#定义全局变量，保存URL保存路径
txtname=""

#漏洞利用的输入文件路径
inputfile=""

#保存漏洞利用的结果输出文件路径
outputfile=""



########################################################################################################################################

#定义主窗口
class new_Zhujiemian(QtWidgets.QWidget, Ui_Zhu_jiemian):
    def __init__(self):
        super(new_Zhujiemian,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Xitongfengong_show)   #点击“系统以及分工简介”，显示相应的界面
        self.url_collect_button.clicked.connect(self.url_caiji_show)  # 点击“URL采集”，显示相应的界面
        self.aspcms_button.clicked.connect(self.Loudongzhengming_show)  # 点击“漏洞证明”，显示相应的界面
        self.md5_button.clicked.connect(self.MD5decrypt_show)  # 点击“MD5解密”，显示相应的界面

    #点击按钮，展示系统分工界面
    def Xitongfengong_show(self):
        Xitongfengong.show()

    # 点击按钮，展示URL采集界面
    def url_caiji_show(self):

        Urlcaiji.show()

    # 点击按钮，展示漏洞证明界面
    def Loudongzhengming_show(self):
        Loudongzhengming.show()

    # 点击按钮，展示MD5解密界面
    def MD5decrypt_show(self):
        MD5Decrypt.show()



#重载系统分工界面
class new_Xitongfengong(QtWidgets.QWidget, Ui_widget):
    def __init__(self):
        super(new_Xitongfengong, self).__init__()
        self.setupUi(self)





#重载URL采集界面
class new_URLcaiji(QtWidgets.QWidget, Ui_URL_caiji):
    def __init__(self):
        super(new_URLcaiji, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.Start_Collect)   #点击按钮，开始采集
        self.pushButton_2.clicked.connect(self.Choose_file)  # 点击按钮，选择保存路径

    #选择保存路径
    def Choose_file(self):
        global txtname
        txtname, selectedfilter1 = QFileDialog.getOpenFileName(
            self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )
        #print(type(txtname))


    #开始进行URL采集
    def Start_Collect(self):
        keyword = str(self.lineEdit.text())
        executor = ThreadPoolExecutor(max_workers=10)  # 定义线程池中的线程个数

        # 创建线程池列表以及规定采集的最大页数
        task_list = [executor.submit(main, keyword, i, txtname) for i in range(0, 40, 10)]

        # 等待线程结束
        if (wait(task_list, timeout=None)):
            #print("采集完毕！")

#        for i in range(0, 750, 10):  # 遍历页数，每次增加10
#            print(i)
#            executor.submit(main, keyword, i, txtname)
#            print(keyword,txtname)

            reply = QMessageBox.information(self,
                                            "恭喜",
                                            "采集完毕！",
                                            QMessageBox.Yes | QMessageBox.No)



        #print("开始采集")

#############################################################################################################################################

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


    #重载漏洞证明界面
class new_Loudongzhengming(QtWidgets.QWidget, Ui_Loudong_Zhengming):
    def __init__(self):
        super(new_Loudongzhengming, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Choose_inputfile)   #点击按钮，选择输入的文件
        self.pushButton_2.clicked.connect(self.Choose_outputfile)    #点击按钮，选择结果保存文件
        self.pushButton_3.clicked.connect(self.Start_exp)     #利用漏洞获取用户名和MD5值

        # 重定向输出
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)


    #def __del__(self):
     #   sys.stdout = sys.__stdout__
      #  sys.stderr = sys.__stderr__


    def Choose_inputfile(self):
            global inputfile
            inputfile, selectedfilter1 = QFileDialog.getOpenFileName(
                self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
            )
        #print(type(inputfile))

    def Choose_outputfile(self):
        global outputfile
        outputfile, selectedfilter1 = QFileDialog.getOpenFileName(
            self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )
        #print(type(outputfile))

    def Start_exp(self):
        executor = ThreadPoolExecutor(max_workers=10)  # 定义线程池中的线程个数
        print("以下是检测出的登录名以及密码MD5值")
        #ASPCMS_EXP(inputfile,outputfile)
        executor.submit(ASPCMS_EXP,inputfile,outputfile)




    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()






#############################################################################################################################################
#MD5解密




    #重载MD5解密界面
class new_MD5Decrypt(QtWidgets.QWidget, Ui_MD5_Decrypt):
    def __init__(self):
        super(new_MD5Decrypt, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.Start_decrypt)


    def Start_decrypt(self):
        #获取屏幕输入的MD5值
        md5=self.Before_Decrypt.text()
        password=MD5_(md5)
        self.textEdit.setText(password)





################################################################################################################################################################33

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    Zhujiemian=new_Zhujiemian()     #定义主窗口对象
    Zhujiemian.show()

    #定义系统分工子窗口
    Xitongfengong=new_Xitongfengong()

    #定义URL采集子窗口
    Urlcaiji=new_URLcaiji()

    #定义漏洞证明子窗口
    Loudongzhengming=new_Loudongzhengming()

    #定义MD5解密窗口
    MD5Decrypt=new_MD5Decrypt()



    sys.exit(app.exec_())  # exec()是指消息进入循环，等待可能的输入进行响应




