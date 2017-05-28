#coding:utf-8
from spider.trip_data_spider.utils.MongoDBUtil import MongodbUtil

class MongoPipeline(object):
    '''
    将爬虫爬回来的数据写入mongoDB
    '''

    def __init__(self):
        self.mongo = MongodbUtil()

    def process_item(self, item, spider):
        collection = item["collection"]
        results = item["results"]
        self.mongo.write(results,collection)
