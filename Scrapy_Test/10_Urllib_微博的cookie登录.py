# @Time : 2021/12/17 20:38 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm

# 适用场景：数据采集的时候  需要绕过登录 然后进入某个页面
# 个人信息页面是utf-8 ，但是还是报错 'utf-8' codec can't decode byte 0xb5 in position 672: invalid start byte
# 因为并没有进入个人信息页面，而是跳转到了登录页面
# 登录页面不是utf-8，所以报错

# 什么情况下访问不成功
# 因为请求头的信息不够  所以访问不成功

import urllib.request

url = 'https://weibo.cn/6411503022/info'

headers = {
# ':authority': 'weibo.cn',
# ':method': 'GET',
# ':path': '/6451491586/info',
# ':scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
#     cookie中携带着你的登录信息，如果有登陆之后的cookie  那么我们就能携带着cookie进入任何页面
'cookie': '_T_WM=24c44910ba98d188fced94ba0da5960e; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFxxfgNNUmXi4YiaYZKr_J_5NHD95QcSh-pSh.pSKncWs4DqcjiqgSXIgvVPcpD; SUB=_2A25MKKG_DeRhGeBK7lMV-S_JwzqIHXVv0s_3rDV6PUJbktCOLXL2kW1NR6e0UHkCGcyvxTYyKB2OV9aloJJ7mUNz; SSOLoginState=1630327279',
# referer  判断当前路径是不是由上一个路径进来的    一般情况下 是做图片防盗链
'referer': 'https://weibo.cn/',
'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发起请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('gb2312')


# 将数据保存到本地
with open('weobo.html','w',encoding='UTF-8') as fp:
    fp.write(content)

