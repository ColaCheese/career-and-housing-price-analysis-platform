# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WorkspiderItem(scrapy.Item):
    # career salary data item

    occupation = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()

class Workspider2Item(scrapy.Item):
    # career direction number data item

    direction = scrapy.Field()
    number = scrapy.Field()
    location = scrapy.Field()

