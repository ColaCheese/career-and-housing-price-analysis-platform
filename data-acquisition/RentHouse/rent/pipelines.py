# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import happybase
# import uuid
# from scrapy.utils.project import get_project_settings


class RentPipeline(object):

    def process_item(self, item, spider):
        return item
