# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class SoldhousePipeline(object):

    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    '''
    save data to MongoDb
    '''

    def __init__(self, mongo_uri, mongo_db, mongo_user, mongo_pwd):
        self.mongo_uri = mongo_uri

        self.mongo_db = mongo_db

        self.mongo_user = mongo_user

        self.mongo_pwd = mongo_pwd

    @classmethod
    def from_crawler(cls, crawler):
        return cls(

            mongo_uri=crawler.settings.get('MONGO_URI'),

            mongo_db=crawler.settings.get('MONGO_DB'),

            mongo_user=crawler.settings.get('MONGO_USER'),

            mongo_pwd=crawler.settings.get('MONGO_PWD')

        )

    def open_spider(self, spider):
        # client=MongoClient("mongodb://user:userpwd@xxx.xxx.xxx.xxx:27017/test")

        # self.client = pymongo.MongoClient("mongodb://"+self.mongo_user+":"+self.mongo_pwd+"@"+self.mongo_uri+":27017/"+self.mongo_db)
        self.client=pymongo.MongoClient("mongodb://admin:root@47.99.179.33:27017/")
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__

        self.db[name].insert(dict(item))

        return item

    def close_spider(self, spider):
        self.client.close()
