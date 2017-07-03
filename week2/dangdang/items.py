# -*- coding: utf-8 -*-

import scrapy

class DangdangItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    comments = scrapy.Field()
    time = scrapy.Field()
    press = scrapy.Field()  #出版社
    price = scrapy.Field()
    discount = scrapy.Field()
    category1 = scrapy.Field()  # 种类(小)
    category2 = scrapy.Field()  # 种类(大)