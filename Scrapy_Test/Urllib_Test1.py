#使用urllib来获取百度首页的源码
import urllib.request

# 定义一个url
url = 'https://www.baidu.com/'

# 2.模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 3.获取响应中的页面的源码 content 内容
# read 返回的是字节形式的二进制数据
# 我们要将二进制数据转换成字符串
# 二进制 --》字符串  解码 decode('编码格式')
content = response.read().decode('utf-8')

# 4.打印数据
print(content)

