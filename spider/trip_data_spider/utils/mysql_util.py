#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import MySQLdb

class MysqlUtil(object):

    def __init__(self):
        #创建连接
        self.conn = MySQLdb.connect(
            host = '127.0.0.1',
            port = 3306,
            user ='root',
            passwd = '1234',
            db = 'carp'
        )
        #创建游标
        self.cur = self.conn.cursor()
        self.conn.set_character_set('utf8')
        self.cur.execute('SET NAMES utf8;')
        self.cur.execute('SET CHARACTER SET utf8;')
        self.cur.execute('SET character_set_connection=utf8;')

    def insert_ly_hot_city(self,value):
        sql = "insert into ly_hot_city (city_name,youji_count,crawl_time,reserve_col1) values(%s,%s,%s,%s);"
        self.cur.execute(sql,value)
        self.conn.commit()

    def insert_ly_city_info(self,value):
        sql = "insert into ly_city (city_id,city_name,city_py,modify_time) values(%s,%s,%s,%s);"
        self.cur.execute(sql, value)
        self.conn.commit()

    def insert_hotel_city_distribution(self,value):
        sql = "insert into hotel_city_distribution (hotel_count_one,hotel_count_two,hotel_count_other,modify_date,reserve_col_1,reserve_col_2,reserve_col_3) values(%s,%s,%s,%s,%s,%s,%s);"
        self.cur.execute(sql, value)
        self.conn.commit()

    def insert_hotel_price_distribution(self,value):
        sql = "insert into hotel_price_distribution (low_hotel_count,middle_hotel_count,height_hotel_count,city_type,modify_date,reserve_col_1) values(%s,%s,%s,%s,%s,%s);"
        self.cur.execute(sql, value)
        self.conn.commit()


if __name__ == '__main__':
    m = MysqlUtil()
    value = ['西安',1,'2017-05-01']
    m.insert_ly_hot_city(value)