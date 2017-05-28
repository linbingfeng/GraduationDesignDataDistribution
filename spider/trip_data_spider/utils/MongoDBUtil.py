# -*- coding: utf-8 -*-
from pymongo import MongoClient

class MongodbUtil(object):

    def __init__(self):
        self.client = MongoClient('127.0.0.1',27017)#连接服务器
        self.db = self.client['spider']#连接数据库
        self.collection = ""#连接collection

    def data_count(self,collection):
        self.collection = self.db[collection]
        count = self.collection.count({})
        return count

    def remove_data(self,collection,filter=None):
        if filter:
            self.db[collection].remove(filter)
        else:
            self.db[collection].remove({})

    def over_write(self,item,collection):
        self.db[collection].remove({})
        self.collection = self.db[collection]
        self.collection.insert(item)

    def write(self,item,collection):
        '''向mongoDB写入一条数据'''
        self.collection = self.db[collection]
        self.collection.insert(item)

    def delete(self,collection):
        '''删除mongoDB中的collection'''
        self.collection = self.db[collection]
        self.collection.drop()

    def query(self,collection,filter=None):
        if filter:
            self.collection = self.db[collection]
            return self.collection.find(filter)
        else:
            self.collection = self.db[collection]
            return self.collection.find({})