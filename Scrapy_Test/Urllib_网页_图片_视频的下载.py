import urllib.request

# 下载网页
url_page = 'https://www.sogou.com/'

# urlretrieve() 中参数：url代表下载的路径  filename文件的名字
# 在python中 可以写变量的名字，也可以直接写值
urllib.request.urlretrieve(url_page,'sougou.html')

# 下载图片
url_img = 'https://i01piccdn.sogoucdn.com/e18d35807f0fbeaf'
urllib.request.urlretrieve(url = url_img,filename='lisa.jpg')


# 下载视频
url_video = 'https://www.ixigua.com/7c75b4d8-c6e2-4bee-afd8-462e84db9801'
urllib.request.urlretrieve(url_video,'yyds.mp4')
