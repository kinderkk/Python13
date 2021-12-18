# @Time : 2021/12/17 19:43 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm

# 第一页  http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 合肥
# pid:
# pageIndex: 1
# pageSize: 10

# 第二页  http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 合肥
# pid:
# pageIndex: 2
# pageSize: 10

# post
import urllib.request
import urllib.parse

def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': '合肥',
        'pid':'',
        'pageIndex': page,
        'pageSize': '10'
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664.45Safari / 537.36'
    }
    request = urllib.request.Request(url=base_url,data=data,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('kfc_' + str(page) + '.json','w',encoding='utf-8') as fp:
        fp.write(content)






if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页码'))

    for page in range(start_page,end_page+1):
    #   请求对象的定制
        request = create_request(page)
    #   获取网页的源码
        content = get_content(request)
    #   下载
        down_load(page,content)
