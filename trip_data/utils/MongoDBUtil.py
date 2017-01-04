# -*- coding: utf-8 -*-
from pymongo import MongoClient

class MongodbUtil(object):

    def __init__(self):
        self.client = MongoClient('127.0.0.1',27017)#连接服务器
        self.db = self.client['spider']#连接数据库
        self.collection = ""#连接collection

    def write(self,item,collection):
        '''向mongoDB写入一条数据'''
        self.collection = self.db[collection]
        self.collection.insert(item)

    def delete(self,collection):
        '''删除mongoDB中的collection'''
        self.collection = self.db[collection]
        self.collection.drop()

    def query(self,collection):
        self.collection = self.db[collection]
        return self.collection.find({})