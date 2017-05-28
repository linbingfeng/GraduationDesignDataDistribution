# -*- coding: utf-8 -*-
import  time

from spider.trip_data_spider.utils import log_util
from spider.data_analysis.parent_class.distribution import Distribution

class Start(Distribution):


    def run(self,date):
        for item in self.mongo.query("ly_pc_city",{"crawl_date":date}):
            value = [item["city_id"],item['city_name'],item['city_name_en'],item["crawl_date"]]
            self.mysql.insert_ly_city_info(value)

if __name__ == '__main__':
    log_util.info("写入城市信息开始")
    s = Start()
    date = time.strftime("%Y-%m-%d",time.localtime())
    s.run(date)
    log_util.info("写入城市信息结束")
