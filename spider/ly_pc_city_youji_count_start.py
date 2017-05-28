# -*- coding: utf-8 -*-
import sys
import os
import time

from scrapy.cmdline import execute

from trip_data_spider import conf

class Start():

    def __init__(self):
        self.log_path = conf.log_path

    def run(self,date):
        log_path = self.log_path + '/LyPcCityYoujiCountSpider/spider_log_' + str(int(time.time()))
        dir_path = self.log_path + r'/LyPcCityYoujiCountSpider'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        sys.argv = ["scrapy", "crawl", "LyPcCityYoujiCountSpider","--logfile="+log_path,'-a','date='+date]
        # sys.argv = ["scrapy", "crawl", "LyPcCityYoujiCountSpider"]
        execute()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        modify_date = time.strftime("%Y-%m-%d", time.localtime())
    else:
        modify_date = sys.argv[1]
    start = Start()
    start.run(modify_date)