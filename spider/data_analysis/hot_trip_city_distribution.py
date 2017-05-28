# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time

from spider.trip_data_spider.utils import log_util
from spider.data_analysis.parent_class.distribution import Distribution

class Start(Distribution):


    def run(self,date):
        log_util.info("城市热度分析开始")
        for item in self.mongo.query("ly_city_youji",{'modify_date':date}):
            # crawl_time = time.strftime("%Y-%m-%d",time.localtime())
            value = [item["city_name"],int(item["youji_count"]),item["modify_date"],item["url"]]
            self.mysql.insert_ly_hot_city(value=value)
        log_util.info("城市热度分析结束")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        date = time.strftime("%Y-%m-%d", time.localtime())
    else:
        date = sys.argv[1]
    hc = Start()
    hc.run(date)