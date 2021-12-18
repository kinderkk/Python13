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

url = 'https://user.qzone.qq.com/2653891262'

headers = {
'cookie': 'RK=iVo9Gkpesu; ptcz=8c5577121f4aa2314fc0c1847d83206991bac7b01448998337e02fe9867241d5; tvfe_boss_uuid=82dff56da8776964; pgv_pvid=4417625996; fqm_pvqid=ba42fd23-5141-4efb-aa9f-03ebb53ce316; _qpsvr_localtk=0.33138295487527114; pgv_info=ssid=s4819125030; uin=o2653891262; skey=@FuRkvHtlm; p_uin=o2653891262; pt4_token=7bev*Ra1nVGxUzPjb3krm1wZUv8gHe3k83*vBDC-kxI_; p_skey=oe5lY*kSkOhQPpyVrJL2pLgIT49SPfsbX3p853hxFfg_; Loading=Yes; qz_screen=1536x864; 2653891262_todaycount=0; 2653891262_totalcount=37747; QZ_FE_WEBP_SUPPORT=1',
'if-modified-since': 'Fri, 17 Dec 2021 13:09:52 GMT',
'referer': 'https://qzs.qq.com/',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'

}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发起请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')


# 将数据保存到本地
with open('qqzone.html','w',encoding='UTF-8') as fp:
    fp.write(content)

