import requests
import json
from lxml import etree

url = "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc&_signature=_02B4Z6wo00d01GxXYcwAAIDBD12hpz29u-Rsc2VAAHq23ItQkFe.iUsU4Ak0VmfgaXW72xgzXgw3u4V5uHQk75xElCWW1FmRg1KfT5P5SyUVO-QA4FCgOPj-7R5xW75vZg08fi5jLnHvW8SD0b"

headers = {
    'Referer': 'https://www.toutiao.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
# print(response.text)

str = response.text
# print(str)

json_str = json.loads(str)
# print(json_str)

event_list = json_str["data"]
# print(event_list)

title_list = []
for i in event_list:
    title_list.append(i["Title"])

# print(title_list)

for i in title_list:
    print(i)



# 豆瓣电影标题
# etree = etree.HTML(response.text)
#
# # print(response.text)
# li_list = etree.xpath('//ol[@class="grid_view"]/li//span[@class="title"][1]/text()')
#
# # print(li_list)
#
# title_list = []
# for i in li_list:
#     print(i)


