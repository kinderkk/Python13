import urllib.request

url = 'https://www.baidu.com/'

# 2.模拟浏览器向服务器发送请求
response  = urllib.request.urlopen(url)

# response 是 'http.client.HTTPResponse'类型
#print(type(response))

# 按照一个一个字节去读
#content = response.read()
#print(content)

# 返回5个字节
#content = response.read(5)
#print(content)

# 读取一行
# content = response.readline()
# print(content)

#
# content = response.readlines()
# print(content)

# 返回状态码 如果是200，就证明我们的逻辑没有错
#print(response.getcode())

# 返回url地址
# print(response.geturl())

# 获取的是一个状态信息
print(response.getheaders())

# 一个类型：HTTPResponse
# 六个方法：read readline readlines getcode geturl getheaders

