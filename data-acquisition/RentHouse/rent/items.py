# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RentItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()  # 租金
    location = scrapy.Field()  # 区域
    city = scrapy.Field()  # 城市名字
    number = scrapy.Field()  # 总数
