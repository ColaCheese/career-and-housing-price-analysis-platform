import happybase
import uuid
from scrapy.utils.project import get_project_settings
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class WorkspiderPipeline(object):
    # 连接hbase
    def __init__(self):
        settings = get_project_settings()
        host = settings['HBASE_HOST']
        table_name = settings['HBASE_TABLE']
        connection = happybase.Connection(host)
        table = connection.table(table_name)
        self.table = table

    def process_item(self, item, spider):
        occupation = item['occupation']
        salary = item['salary']
        location = item['location']
        self.table.put(str(uuid.uuid1()),
                       {
                        'info:location':location,
                        'info:salary': salary,
                        'info:occupation': occupation,
                       }
                       )
        return item
