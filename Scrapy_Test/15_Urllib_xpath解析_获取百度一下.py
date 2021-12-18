# @Time : 2021/12/18 10:19 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm

# 1.获取网页的源码
# 2.解析  解析响应文件  etree.HTML
# 3.打印
import urllib.request

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

# 请求头的定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发起请求
response = urllib.request.urlopen(request)
# 获取内容
content = response.read().decode('utf-8')

# 解析网页源码，获取我们想要的数据
from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据 xpath的返回值是 一个列表类型
result = tree.xpath('//input[@id="su"]/@value')
result = tree.xpath('//input[@id="su"]/@value')[0]
print(result)