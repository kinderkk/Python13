# @Time : 2021/12/18 10:32 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm

# https://sc.chinaz.com/

# 1.请求对象的定制
# 2.获取网页的源码
# 3.下载

# 需求 要下载的是前十页的图片

# 第一页 https://sc.chinaz.com/tupian/meishi.html
# 第二页 https://sc.chinaz.com/tupian/meishi_2.html
# 第二页 https://sc.chinaz.com/tupian/meishi_page.html
import urllib.request
from lxml import etree


def create_request(page):
    if(page == 1):
        url = 'https://sc.chinaz.com/tupian/meishi.html'
    else:
        url = 'https://sc.chinaz.com/tupian/meishi_' + str(page) + '.html'
    print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
#    下载图片
#   urllib.request.urlretrieve('图片地址','文件的名字')
    tree = etree.HTML(content)

    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
#   一般设计图片的网站都会进行懒加载
#    图片没有加载出来之前是src2，加载出来候会变成src
    src_list = tree.xpath('//div[@id="container"]//a/img/@src2')

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src

        urllib.request.urlretrieve(url=url,filename= './data_jpg/' + name + '.jpg')



if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page,end_page+1):
#       请求对象的定制
        request = create_request(page)
#      获取网页的源码
        content = get_content(request)
 #      下载
        down_load(content)
