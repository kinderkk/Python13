# @Time : 2021/12/17 20:28 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm
import urllib.request
# https://blog.csdn.net/qq_33709582/article/details/121900989 假如一不小心写错
# 会报urllib.error.HTTPError: HTTP Error 404: Not Found
url = 'https://blog.csdn.net/qq_33709582/article/details/1219009891'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

try:
    resquest = urllib.request.Request(url=url,headers=headers)

    response = urllib.request.urlopen(resquest)

    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('系统正在升级……')
