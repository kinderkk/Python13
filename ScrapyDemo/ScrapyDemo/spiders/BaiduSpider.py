import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'BaiduSpider'
    allowed_domains = ["baidu.com"]
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print(response.text)
