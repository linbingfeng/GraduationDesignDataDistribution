# -*- coding: utf-8 -*-
import time
import json
from scrapy import Spider
from scrapy import Request
from spider.trip_data_spider.utils.MongoDBUtil import MongodbUtil

class LyPcHotelInfoSpider(Spider):
    name = 'LyPcHotelInfoSpider'
    start_urls = []
    mongo = MongodbUtil()
    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Host": "www.ly.com",
        "Referer": "http://www.ly.com/hotel/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    }
    count = 0
    for item in mongo.query('ly_pc_city'):
        start_urls.append(item)
        count += 1

    def __init__(self,date):
        self.date = date

    def start_requests(self):
         print self.count
         for city in self.start_urls:
             check_in_day = time.strftime("%Y-%m-%d",time.localtime())
             check_out_day = time.strftime("%Y-%m-%d",time.localtime(time.time()+24*60*60))
             meta = {
                 "city":city
             }
             url = "http://www.ly.com/hotel/handler/SearchHandle.json?pageIndex=1&cityId="+city['city_id']+"&cityName="+city['city_name_en']+"&BusinessId=0&sectionId=0&word=&regionPrice=&radius=&star=&chainids=&facility=&orderby=4&isDanbao=&intime=&labelId=0&wordType=0&comedate="+check_in_day+"&leavedate="+check_out_day + "&iid=0.3416426944366522"
             yield Request(url,headers=self.header,dont_filter=True,meta=meta)

    def parse(self, response):
        city = response.meta["city"]
        body = response.body
        if body:
            body = json.loads(body)
            record_num = body['recordNum']
            for i in range(record_num):
                meta = {
                    "city": city
                }
                check_in_day = time.strftime("%Y-%m-%d", time.localtime())
                check_out_day = time.strftime("%Y-%m-%d", time.localtime(time.time() + 24 * 60 * 60))
                url = "http://www.ly.com/hotel/handler/SearchHandle.json?pageIndex="+str(i+1)+"&cityId=" + city['city_id'] + "&cityName=" + city['city_name_en'] + "&BusinessId=0&sectionId=0&word=&regionPrice=&radius=&star=&chainids=&facility=&orderby=4&isDanbao=&intime=&labelId=0&wordType=0&comedate=" + check_in_day + "&leavedate=" + check_out_day + "&iid=0.3416426944366522"
                header = self.header
                header["Referer"] = "http://www.ly.com/searchlist.html?cityid="+city["city_id"]+"&sectionid=0&comedate="+check_in_day+"&leavedate="+check_out_day+"&word=&wordid=0&wordtype=0&spm0=10002.2001.1.0.1.1.2"
                yield Request(url, headers=self.header, dont_filter=True,callback=self.parse_hotel,meta=meta)

    def parse_hotel(self,response):
        city = response.meta["city"]
        body = response.body
        if body:
            body = json.loads(body)
            hotel_list = body["hotelList"]
            for h in hotel_list:
                item = {
                    "city_name":city["city_name"],
                    "city_id": city["city_id"],
                    "city_name_en": city["city_name_en"],
                    "crawl_time":self.date
                }
                item["hotel_name"] = h["Name"]
                item["hotel_id"] = h["Id"]
                item["price"] = h["LowestPrice"]
                results_item = {
                    "collection":'ly_pc_hotel',
                    "results":item
                }
                yield results_item