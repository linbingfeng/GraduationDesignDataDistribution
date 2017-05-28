# coding=utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

from scrapy import Request
import scrapy
import time
from spider.trip_data_spider.utils.MongoDBUtil import MongodbUtil


class LyPcCityIdSpider(scrapy.Spider):
    name = "LyPcCitySpider"
    start_urls = []
    header = {
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Host":"www.ly.com",
            "Referer":"http://www.ly.com/hotel/",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    }
    mongo = MongodbUtil()
    def __init__(self,date):
        self.date = date

    def start_requests(self):
        url = "http://www.ly.com/hotel/handler/stayincity.json"
        yield Request(url,headers=self.header,dont_filter=True)

    def parse(self, response):
        body = response.body
        if body:
            body = eval(body)
            for i in range(len(body)):
                item = {}
                if body[i][2] is '0':
                    item["city_name"] = body[i][1]
                    item["city_id"] = body[i][0]
                    item["city_name_en"] = body[i][3]
                    item["crawl_date"] = self.date
                    results_item = {}
                    results_item["results"] = item
                    results_item["collection"] = "ly_pc_city"
                    yield results_item
