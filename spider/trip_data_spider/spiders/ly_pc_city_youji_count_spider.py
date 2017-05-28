# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
import time

from scrapy import Request
import scrapy
from spider.trip_data_spider.utils.MongoDBUtil import MongodbUtil


class LyPcCityYoujiCountSpider(scrapy.Spider):
    name = "LyPcCityYoujiCountSpider"
    start_urls = []
    header = {
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Connection":"keep-alive",
        "Host":"www.ly.com",
        "Referer":"http://www.ly.com/travels/travel/searchResult?k=%25E5%25B9%25BF%25E5%25B7%259E&rt=2",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest"
    }
    mongo = MongodbUtil()
    for city in mongo.query("ly_pc_city"):
        start_urls.append(city)

    def __init__(self,date):
        self.modify_date = date

    def start_requests(self):
        for city in self.start_urls:
            if city:
                url = "http://www.ly.com/travels/travel/getSearchYouJiList?k={}&pindex=1&psize=10&rt=1&iid=0.9630197338701016".format(city.get("city_name"))
                self.header["Referer"] = "http://www.ly.com/travels/travel/searchResult?k={}&rt=2".format(city.get("city_name"))
                meta = {
                    "city":city
                }
                yield Request(url,headers=self.header,dont_filter=True,meta=meta)

    def parse(self, response):
        city = response.meta["city"]
        city_name = city.get("city_name")
        body = response.body
        body = json.loads(body)
        youji_info = {
            "youji_count":body.get("yCount"),
            "city_name":city_name,
            "url":"http://www.ly.com/go/area/"+city["city_id"]+".html",
            "modify_date":self.modify_date
        }
        item = {
            "collection":"ly_city_youji",
            "results":youji_info
        }
        yield item
