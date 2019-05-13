from bs4 import BeautifulSoup as bs
import requests
import hashlib
from urllib.parse import urljoin
import re

def MD5_(md5):

    url = "https://www.somd5.com/search.php"  # 请求的MD5解密网址
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko'}
    data={
        'hash':md5,               #传入MD5值
        'captcha':'0'
    }

    r = requests.post(url=url, data=data,headers=headers)  # 请求目标网址
    #获取到的返回值
    password=r.content
    #对获取到的值进行相应的UTF8解码
    password=password.decode()
    #将password转化为字典
    password=eval(password)
    #获取密码
    password_final=password['data']
    return password_final
    print(password_final)





if __name__=="__main__":
    MD5()

