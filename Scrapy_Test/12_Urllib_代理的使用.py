# @Time : 2021/12/17 22:01 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm

import urllib.request

url = 'http://ip111.cn/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)
# 快代理  https://www.kuaidaili.com/free/
proxies = {
    'http':'ip:端口号'
}

# handler builder_opener  open
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

# response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)