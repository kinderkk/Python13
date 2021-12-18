import scrapy
import json


class JDSpider(scrapy.Spider):
    name = 'JDSpider'
    allowed_domains = ['jd.com']

# 通过设置请求头，伪装成浏览器
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    # start_urls = ['https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10037728331339&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1']
    # 手动发起请求
    def start_requests(self):
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10037728331339&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
        # callback回调函数，设置由那个函数去解析response
        # yield 生成器
        #
        yield scrapy.Request(url, headers = self.headers,callback=self.parsecomment)


    def parsecomment(self, response):
        print(response.text)
