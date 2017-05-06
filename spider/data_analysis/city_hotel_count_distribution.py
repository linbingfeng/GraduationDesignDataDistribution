#coding:utf-8
from spider.data_analysis.parent_class.distribution import Distribution

class Start(Distribution):

    def run(self,date):
        city_dict= {}
        for item in self.mongo.query("ly_pc_hotel",{"crawl_time" : date}):
            city_id = item['city_id']
            if not city_dict.get(city_id):
                info = {
                    'city_id':item['city_id'],
                    'city_name': item['city_name'],
                    'city_py': item['city_name_en'],
                    'hotel_count':0,
                    'low_hotel_count':0,
                    'middle_hotel_count':0,
                    'height_hotel_count':0,
                    'integral':0
                }
                city_dict[city_id] = info
            city_dict[city_id]['hotel_count'] += 1
            if int(item['price']) >= 5000:
                city_dict[city_id]['height_hotel_count'] += 1
                city_dict[city_id]['integral'] += 10
            elif int(item['price']) >= 3000:
                city_dict[city_id]['height_hotel_count'] += 1
                city_dict[city_id]['integral'] += 7
            elif int(item['price']) >= 1800:
                city_dict[city_id]['height_hotel_count'] += 1
                city_dict[city_id]['integral'] += 5
            elif int(item['price']) >= 1200:
                city_dict[city_id]['height_hotel_count'] += 1
                city_dict[city_id]['integral'] += 4
            elif int(item['price']) >= 800:
                city_dict[city_id]['height_hotel_count'] += 1
                city_dict[city_id]['integral'] += 3
            elif int(item['price']) >= 300:
                city_dict[city_id]['middle_hotel_count'] += 1
                city_dict[city_id]['integral'] += 2
            else:
                city_dict[city_id]['low_hotel_count'] += 1
                city_dict[city_id]['integral'] += 1
        for city_id in city_dict:
            item = city_dict.get(city_id)
            value = [item['hotel_count'],item['low_hotel_count'],item['middle_hotel_count'],item['height_hotel_count'],item['integral'],city_id,date]
            sql = "update city_hotel_count set hotel_count=%s,low_hotel_count=%s,middle_hotel_count=%s,height_hotel_count=%s,integral=%s where city_id=%s and crawl_date=%s"
            self.mysql.cur.execute(sql, value)
            self.mysql.conn.commit()
        self.mysql.cur.close()
        self.mysql.conn.close()

if __name__ == '__main__':
    s = Start()
    date = '2017-05-04'
    s.run(date)