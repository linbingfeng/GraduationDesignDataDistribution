#coding:utf-8
from spider.trip_data_spider.utils.MongoDBUtil import MongodbUtil
from spider.trip_data_spider.utils.mysql_util import MysqlUtil
from spider.trip_data_spider.utils import log_util

class CityHotelCountInit(object):

    def __init__(self):
        self.mongo = MongodbUtil()
        self.mysql = MysqlUtil()
        self.city_count = 0

    def run(self,date):
        log_util.info('城市初始化开始')
        for item in self.mongo.query('ly_pc_city'):
            sql = "insert into city_hotel_count (city_id,city_name,city_py,crawl_date) values(%s,%s,%s,%s)"
            value = [item['city_id'],item['city_name'],item['city_name_en'],date]
            self.mysql.cur.execute(sql,value)
            self.mysql.conn.commit()
            self.city_count += 1
        self.mysql.cur.close()
        self.mysql.conn.close()
        log_util.info('城市初始化结束')
        log_util.info("city_count:"+str(self.city_count))


if __name__ == '__main__':
    c = CityHotelCountInit()
    # c.run('2017-05-03')
    c.run('2017-05-04')