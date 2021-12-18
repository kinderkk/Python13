# @Time : 2021/12/17 21:50 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm

# 需求：使用handler来访问百度  获取网页源码

import urllib.request

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

# handler  build_opener   open
# 1.获取handler对象
handler = urllib.request.HTTPHandler()

# 2.获取opener对象
opener = urllib.request.build_opener(handler)

# 3.调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')
print(content)


