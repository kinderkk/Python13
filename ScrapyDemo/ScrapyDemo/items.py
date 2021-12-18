# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 明确爬取目标的格式
class CommentItem(scrapy.Item):
    id = scrapy.Field()
    content = scrapy.Field()
    creationTime = scrapy.Field()
    score = scrapy.Field()
    nickname = scrapy.Field()


