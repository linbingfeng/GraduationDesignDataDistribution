# -*- coding: utf-8 -*-
import time
from pymongo import MongoClient
from spider.trip_data_spider.utils import log_util
from spider.data_analysis.parent_class.distribution import Distribution

class Start(Distribution):
    client = MongoClient('127.0.0.1', 27017)  # 连接服务器
    db = client['spider']  # 连接数据库
    collection = db["ly_pc_hotel"]  # 连接collection

    def run(self,date):
        hotel_num = self.collection.count({"crawl_time":date})
        one_city = [u'北京',u'上海',u'广州',u'深圳']
        two_city = [u'天津',u'南京',u'武汉',u'沈阳',u'西安',u'重庆',u'杭州',u'青岛',u'大连',u'宁波',u'济南',u'哈尔滨',u'长春',u'厦门',u'郑州',u'长沙',u'福州',u'乌鲁木齐',u'昆明',u'兰州',u'苏州',u'无锡',u'南昌',u'贵阳',u'南宁',u'合肥',u'太原',u'石家庄',u'呼和浩特',u'佛山',u'东莞',u'唐山',u'烟台',u'泉州',u'包头']
        city_item = {
            "hotel_num":hotel_num,
            "one_city_num" :0,
            "two_city_num": 0,
            "other_city_num": 0,
            "time":date
        }
        one_price_item = {
            "type":1,
            "hotel_num":0,
            "height_num": 0,
            "middle_num": 0,
            "low_num": 0,
            "time": date
        }
        two_price_item = {
            "type": 2,
            "hotel_num": 0,
            "height_num": 0,
            "middle_num": 0,
            "low_num": 0,
            "time": date
        }
        other_price_item = {
            "type": 3,
            "hotel_num": 0,
            "height_num": 0,
            "middle_num": 0,
            "low_num": 0,
            "time": date
        }
        for hotel in self.collection.find({"crawl_time":date}):
            if hotel["city_name"] in one_city:
                city_item["one_city_num"] = city_item["one_city_num"] + 1
                if int(hotel["price"]) != 0:
                    one_price_item["hotel_num"] = one_price_item["hotel_num"] + 1
                    if int(hotel["price"]) < 100:
                        one_price_item["low_num"] = one_price_item["low_num"] + 1
                    elif int(hotel["price"]) >= 100 and int(hotel["price"]) < 300:
                        one_price_item["middle_num"] = one_price_item["middle_num"] + 1
                    else:
                        one_price_item["height_num"] = one_price_item["height_num"] + 1
            elif hotel["city_name"] in two_city:
                city_item["two_city_num"] = city_item["two_city_num"] + 1
                if int(hotel["price"]) != 0:
                    two_price_item["hotel_num"] = two_price_item["hotel_num"] + 1
                    if int(hotel["price"]) < 100:
                        two_price_item["low_num"] = two_price_item["low_num"] + 1
                    elif int(hotel["price"]) >= 100 and int(hotel["price"]) < 300:
                        two_price_item["middle_num"] = two_price_item["middle_num"] + 1
                    else:
                        two_price_item["height_num"] = two_price_item["height_num"] + 1
            else:
                city_item["other_city_num"] = city_item["other_city_num"] + 1
                if int(hotel["price"]) != 0:
                    other_price_item["hotel_num"] = other_price_item["hotel_num"] + 1
                    if int(hotel["price"]) < 300:
                        other_price_item["low_num"] = other_price_item["low_num"] + 1
                    elif int(hotel["price"]) >= 300 and int(hotel["price"]) < 800:
                        other_price_item["middle_num"] = other_price_item["middle_num"] + 1
                    else:
                        other_price_item["height_num"] = other_price_item["height_num"] + 1
        self.mongo.write(city_item,'ly_hotel_city_distribution')
        self.mongo.write(one_price_item, 'ly_hotel_price_distribution')
        self.mongo.write(two_price_item, 'ly_hotel_price_distribution')
        self.mongo.write(other_price_item, 'ly_hotel_price_distribution')

    def hotel_city_distribution_2_mysql(self,date):
        for item in self.mongo.query("ly_hotel_city_distribution",{"time":date}):
            per_one =round(float(item["one_city_num"])/float((item["one_city_num"]+item["two_city_num"]+item["other_city_num"]))*100,2)
            per_two = round(float(item["two_city_num"])/float((item["one_city_num"]+item["two_city_num"]+item["other_city_num"]))*100,2)
            per_other = round(float(item["other_city_num"])/float((item["one_city_num"]+item["two_city_num"]+item["other_city_num"]))*100,2)
            value = [item["one_city_num"],item["two_city_num"],item["other_city_num"],item["time"],per_one,per_two,per_other]
            self.mysql.insert_hotel_city_distribution(value)

    def hotel_price_distribution_2_mysql(self,date):
        for item in self.mongo.query("ly_hotel_price_distribution",{"time":date}):
            value = [item["low_num"], item["middle_num"], item["height_num"], item["type"],item["time"],item["hotel_num"]]
            self.mysql.insert_hotel_price_distribution(value)

if __name__ == '__main__':
    log_util.info("酒店分布分析开始")
    h = Start()
    # date = time.strftime("%Y-%m-%d",time.localtime())
    date = '2017-05-04'
    h.run(date)
    h.hotel_city_distribution_2_mysql(date)
    h.hotel_price_distribution_2_mysql(date)
    log_util.info("酒店分布分析结束")