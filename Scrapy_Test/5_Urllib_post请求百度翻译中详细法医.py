# @Time : 2021/12/17 15:38 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm

import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Accept': '*/*,',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '133',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=E98C8FF7E52CC345DB15042EDF78CBA2; PSTM=1634135062; BAIDUID=E98C8FF7E52CC34587F47559A930F5A6:FG=1; __yjs_duid=1_b9ed1de6a66a5ce7adc4941f9b8601861634301936766; BDUSS=0JwYkh6Wm1IblNKM0QwS0k5R3d2eVBOYU53THUxOEFqTndub2lwRFgxTHF0cXBoSUFBQUFBJCQAAAAAAAAAAAEAAABslQCrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOopg2HqKYNhS; BDUSS_BFESS=0JwYkh6Wm1IblNKM0QwS0k5R3d2eVBOYU53THUxOEFqTndub2lwRFgxTHF0cXBoSUFBQUFBJCQAAAAAAAAAAAEAAABslQCrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOopg2HqKYNhS; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=ciIOJexroG040L7HxgxPMhsmjgKK0gOTDYLEUamaI2AU2V4VgK9uEG0Pt_U-mEt-J8jwogKKWmOTH7kF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbkD_C-MfIvDqTrP-trf5DCShUFs54omB2Q-XPoO3KtMhh46yb7J5qkIMhbLatbiWbRM2MbgylRp8P3y0bb2DUA1y4vpKMP8bmTxoUJ2XMKVDq5mqfCWMR-ebPRiL-r9Qg-fBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hI0ljj82e5PVKgTa54cbb4o2WbCQ5x5r8pcN2b5oQTO3D-kfBnvMbmQuBPOE2J3vOIJTXpOUWfAkXpJvQnJjt2JxaqRC5hkBfq5jDh3MBpQDhtoJexIO2jvy0hvcQb6cShP6MUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDNtDt60jfn3aQ5rtKRTffjrnhPF3M-LfXP6-hnjy3b4Jop45WPnJfqnEMbbVM4-UyN3MWh3RymJ42-39LPO2hpRjyxv4bUn-5toxJpOJXaILWl52HlFWj43vbURv3Pug3-AfaM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoK0hJC-2bKvPKITD-tFO5eT22-usM6TR2hcHMPoosItmDMkbybks5tnuanJL2DviaKJjBMbUoqRHXnJi0btQDPvxBf7p5208Ll5TtUJM_UKzhfoMqfTbMlJyKMniQKj9-pP52hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDTtajj3QeaRt2tcyatj2WnTJ25r8e5rnhPF3-PFPXP6-hnjy3b4Jop45WPnJJMJEMbbVM4-UyN3MWh3RymJ4-RjEKlIKEfK436O4bUn-5toxJpOJXaILWl52HlFWj43vbURv3Pug3-AfaM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqC_WhK0G3j; BDSFRCVID_BFESS=ciIOJexroG040L7HxgxPMhsmjgKK0gOTDYLEUamaI2AU2V4VgK9uEG0Pt_U-mEt-J8jwogKKWmOTH7kF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbkD_C-MfIvDqTrP-trf5DCShUFs54omB2Q-XPoO3KtMhh46yb7J5qkIMhbLatbiWbRM2MbgylRp8P3y0bb2DUA1y4vpKMP8bmTxoUJ2XMKVDq5mqfCWMR-ebPRiL-r9Qg-fBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hI0ljj82e5PVKgTa54cbb4o2WbCQ5x5r8pcN2b5oQTO3D-kfBnvMbmQuBPOE2J3vOIJTXpOUWfAkXpJvQnJjt2JxaqRC5hkBfq5jDh3MBpQDhtoJexIO2jvy0hvcQb6cShP6MUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDNtDt60jfn3aQ5rtKRTffjrnhPF3M-LfXP6-hnjy3b4Jop45WPnJfqnEMbbVM4-UyN3MWh3RymJ42-39LPO2hpRjyxv4bUn-5toxJpOJXaILWl52HlFWj43vbURv3Pug3-AfaM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoK0hJC-2bKvPKITD-tFO5eT22-usM6TR2hcHMPoosItmDMkbybks5tnuanJL2DviaKJjBMbUoqRHXnJi0btQDPvxBf7p5208Ll5TtUJM_UKzhfoMqfTbMlJyKMniQKj9-pP52hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDTtajj3QeaRt2tcyatj2WnTJ25r8e5rnhPF3-PFPXP6-hnjy3b4Jop45WPnJJMJEMbbVM4-UyN3MWh3RymJ4-RjEKlIKEfK436O4bUn-5toxJpOJXaILWl52HlFWj43vbURv3Pug3-AfaM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqC_WhK0G3j; delPer=0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BAIDUID_BFESS=3997CC162DAB5E5855CB84B661DA39EC:FG=1; PSINO=6; H_PS_PSSID=35295_35106_31253_35456_34584_35490_35324_26350; BA_HECTOR=a40hag80ag04aga0ne1grofbs0q; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1639724087,1639724193,1639725210,1639726464; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1639726464; __yjs_st=2_YWQyZGRkOThlNWE2OTU2NWMwYmE3NjM4NjgwNTYwMDMyYWQyZGUxNGY5ZGVhYTYxODAzYzRlN2Q5YTIyMmFkN2U4MTJmZDVmMzUyYmFiY2M5YjViYTI4MDA5YWIzNDU1YjRiZDQzYTM1YzM3MzNjMTJjMGM0YTczMmUwZjdiYmMxMjcwYzc2YWI5ODgwMjIwZDNhZjEzZDQzZTFjOWYxYjY0MjcxYTk2NWEyMjk4NTA3MTQ5NGZiNGVkNDUyNGQ2OGFhODMxNTlhMmQwYzg0MmIxNGE5YzkyNTk1Nzg5N2E5ZWY1YThkMjI5ZjVjNDdlZDQ4MmU5OGY0NDdiOWYyNl83XzgxMWIyMGI2; ab_sr=1.0.1_ZmUxNmVlODRkMDQ3NmI2MjdiYzc2MThhZWMwN2FiMTUzODkxZWFjZDk0YTExNmQ2YmRkMmVmODUxNWUxOGY3ZjYzZGE5NmMyMjM5ZjFmYjgzZTYzYmJjNTM3MTQ5YjE0YWI2OTIwNGExODhkMDRmODdlNzdkZjU4YzI0NDY2MmNhMjUwYTM0ZGZhMDc2YjczMTlkZDg1OWVhOGRlMDAwYmFlZGNmM2I4MDBiOTlmODA4OTNiZjBjZGUxNzZkYmJj',
    # 'Host': 'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer':' https://fanyi.baidu.com/?aldtype=16047',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode':' cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'lo',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '646722.867699',
    'token': '82d3cd9eec8e681ec766d345a86b287f',
    'domain': 'common'
}

#post 请求的参数必须要进行编码，并且调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
request  = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
conent = response.read().decode('utf-8')


import json
obj = json.loads(conent)
print(obj)