# @Time : 2021/12/18 16:14 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm

import urllib.request

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')

name_list = soup.select('')

