# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render
from trip_data.utils.MongoDBUtil import MongodbUtil

def index(request):
    mongo = MongodbUtil()
    context = {}
    context['hello'] = 'Hello World!'
    city_d = []
    price_d = []
    for city in mongo.query('ly_hotel_city_distribution'):
        city_d.append(city)
    for p in mongo.query('ly_hotel_price_distribution'):
        price_d.append(p)
    context["city_data"] = city_d
    context["price_data"] = price_d
    context["one"] = round(float(city_d[0]["one_city_num"]) / float(city_d[0]["hotel_num"])*100,2)
    context["two"] = round(float(city_d[0]["two_city_num"]) / float(city_d[0]["hotel_num"])*100,2)
    context["other"] = round(float(city_d[0]["other_city_num"]) / float(city_d[0]["hotel_num"])*100,2)
    context["has_price_hotel"] = price_d[0]["hotel_num"]+price_d[1]["hotel_num"]+price_d[2]["hotel_num"]
    context["all_low_hotel"] = price_d[0]["low_num"]+price_d[1]["low_num"]+price_d[2]["low_num"]
    context["all_middle_hotel"] = price_d[0]["middle_num"] + price_d[1]["middle_num"] + price_d[2]["middle_num"]
    context["all_height_hotel"] = price_d[0]["height_num"] + price_d[1]["height_num"] + price_d[2]["height_num"]
    return render(request, 'index.html', context)