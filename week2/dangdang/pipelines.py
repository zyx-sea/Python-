# -*- coding: utf-8 -*-
import pymongo
from scrapy.conf import settings
from .items import DangdangItem

class DangdangPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host,port=port)
        tdb = client[db_name]
        self.post = tdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        '''先判断itme类型，在放入相应数据库'''
        if isinstance(item,DangdangItem):
            try:
                book_info = dict(item)  #
                if self.post.insert(book_info):
            except Exception:
                pass
        return item