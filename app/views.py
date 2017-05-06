#coding:utf-8
import time

from django.shortcuts import render

from app.models import LyHotCity
from app.models import HotelCityDistribution
from app.models import HotelPriceDistribution
from app.models import CityHotelCount

# Create your views here.
def hot_city(request):
    context = {
        'data':[],
        'pindex':1,
        'psize':30,
        'pcount':0,
        'date':str(time.strftime("%Y-%m-%d",time.localtime())),
        'y':str(time.strftime("%Y-%m-%d",time.localtime())).split("-")[0],
        'm': str(time.strftime("%Y-%m-%d", time.localtime())).split("-")[1],
        'd': str(time.strftime("%Y-%m-%d", time.localtime())).split("-")[2],
    }
    if 'date' in request.GET:
        context['date'] = str(request.GET['date'])
        s = context['date'].split('-')
        context['y'] = s[0]
        context['m'] = s[1]
        context['d'] = s[2]
    if 'pindex' in request.GET:
        context['pindex'] = int(request.GET['pindex'])
        context['psize'] = int(request.GET['psize'])
    if context['psize'] > 36 or context['psize'] < 5:
        context['psize'] = 30
    pcount = LyHotCity.objects.filter(crawl_time=context['date']).count() / context['psize']
    if pcount%context['psize']==0:
        context['pcount'] = pcount
    else:
        context['pcount'] = pcount+1

    if context['pindex'] <= 0 or context['pindex'] > context['pcount']:
        context['pindex'] = 1

    start = (context['pindex'] - 1) * context['psize']
    end = start + context['psize']
    response = LyHotCity.objects.filter(crawl_time=context['date']).order_by('-youji_count')[start:end]
    for item in response:
        context['data'].append(item)
    return render(request, 'hot_city.html', context)


def hotel_distribution(request):
    date = time.strftime("%Y-%m-%d",time.localtime())
    if 'date' in request.GET:
        date = request.GET['date']
    if not date:
        date = time.strftime("%Y-%m-%d", time.localtime())
    response_city = HotelCityDistribution.objects.filter(modify_date=date)
    response_price= HotelPriceDistribution.objects.filter(modify_date=date)
    price_data = []
    city_data = []
    city_data_count = 0
    for city in response_city:
        city_data_count = city.hotel_count_one+city.hotel_count_two+city.hotel_count_other
        city_data = city
    has_price_hotel = [0,0,0,0]
    for item in response_price:
        price_data.append(item)
        has_price_hotel[0] += int(item.reserve_col_1)
        has_price_hotel[1] += item.low_hotel_count
        has_price_hotel[2] += item.middle_hotel_count
        has_price_hotel[3] += item.height_hotel_count
    context = {
        'city_data': city_data,
        'city_data_count':city_data_count,
        'price_data': price_data,
        'has_price_hotel':has_price_hotel,
        'y':date.split("-")[0],
        'm':date.split("-")[1],
        'd':date.split("-")[2],
    }
    return render(request, 'hotel_distribution.html', context)

def city_economic(request):
    context = {
        'data': [],
        'pindex': 1,
        'psize': 10,
        'pcount': 0,
        'date': str(time.strftime("%Y-%m-%d", time.localtime())),
        'y': str(time.strftime("%Y-%m-%d", time.localtime())).split("-")[0],
        'm': str(time.strftime("%Y-%m-%d", time.localtime())).split("-")[1],
        'd': str(time.strftime("%Y-%m-%d", time.localtime())).split("-")[2],
    }
    if 'date' in request.GET:
        context['date'] = request.GET['date']
    if 'pindex' in request.GET:
        context['pindex'] = int(request.GET['pindex'])
    if 'psize' in request.GET:
        context['psize'] = int(request.GET['psize'])
    else:
        context['psize'] = 10
    if context['psize'] > 36 or context['psize'] < 5:
        context['psize'] = 10
    pcount = CityHotelCount.objects.filter(crawl_date=context['date']).count() / context['psize']
    if pcount % context['psize'] == 0:
        context['pcount'] = pcount
    else:
        context['pcount'] = pcount + 1
    if context['pindex'] <= 0 or context['pindex'] > context['pcount']:
        context['pindex'] = 1
    start = (context['pindex'] - 1) * context['psize']
    end = start + context['psize']
    response = CityHotelCount.objects.filter(crawl_date=context['date']).order_by('-integral')[start:end]
    ranking = 0
    for item in response:
        ranking += 1
        item.reserve_col_1 = ranking + (context['pindex']-1)*context['psize']
        context['data'].append(item)
    # if not context['data']:
    #     context['date'] = str(time.strftime("%Y-%m-%d", time.localtime()))
    #     context['pcount'] = CityHotelCount.objects.filter(crawl_date=context['date']).count() / context['psize']
    return render(request, 'city_economic.html', context)