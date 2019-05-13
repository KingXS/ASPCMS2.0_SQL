import requests
from bs4 import BeautifulSoup as bs   #将模块重命名
import re
from concurrent.futures import ThreadPoolExecutor,wait
import time
import os
import sys


def main(keyword, i, txtname):
    url = 'https://www.baidu.com/s?wd=%s&pn=%s' % (str(keyword), str(i))  # 定义URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko'}
    r = requests.get(url=url, headers=headers)  # 请求目标网址
    soup = bs(r.content, 'lxml')  # 利用BS解析网址
    urls = soup.find_all(name='a',
                         attrs={'data-click': re.compile(('.')), 'class': None})  # 利用bs提取标签为a，属性class为None的所有内容

    for url in urls:
        # print(url['href'])  #取出href中的链接内容
        try:
            r_get_url = requests.get(url=url['href'], headers=headers, timeout=4)  # 发送请求，看是否能够正常打开网站
            if r_get_url.status_code == 200:  # 判断状态码是否是200
                url_para = r_get_url.url  # 获取状态码为200的链接
                url_index_tmp = url_para.split('/')  # 以‘/’为分隔符分割url
                url_index = url_index_tmp[0] + '//' + url_index_tmp[2] + '\n'  # 将分割后的网址重新拼凑成标准的格式
                url_save = open(txtname, "a+")
                url_save.write(url_index)
                #print(url_index)  # 获得网站的状态码
        except Exception as e:  # 如果网站请求异常，则直接跳过
            pass




