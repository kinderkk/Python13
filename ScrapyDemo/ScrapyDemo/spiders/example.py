import scrapy


class ExampleSpider(scrapy.Spider):
    # 爬虫的名称，用于启动爬虫
    name = 'example'
    # 设置允许爬取的域名
    allowed_domains = ['example.com']
    #启动的url
    start_urls = ['http://example.com/']

    #解析函数
    def parse(self, response):
        pass
