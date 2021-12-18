import urllib.request

url = 'https://www.baidu.com/'

#url的组成
# http 与 https  www.baidu.com
#    协议              主机      端口号  路径  参数  锚点
# http 80
# https 443
# mysql 3306
# oracle 1521
# redis 6379
# 因为有些网站需要 UA 检验，普通的爬虫就不得行了，需要升级
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

# 因为urlopen方法中不能存储字典，所以header不能传进去
# 请求对象的定制
# 因为参数顺序的问题，不能直接写url与headers
request  = urllib.request.Request(url = url,headers = headers)


url = 'https://www.baidu.com/'

response = urllib.request.urlopen(url)
content = response.read().decode('utf_8')

print(content)


