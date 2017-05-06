#coding:utf-8
from spider.trip_data_spider.utils.MongoDBUtil import MongodbUtil
from spider.trip_data_spider.utils.mysql_util import MysqlUtil

class Distribution(object):

    def __init__(self):
        self.mongo = MongodbUtil()
        self.mysql = MysqlUtil()

    def run(self,date):
        pass