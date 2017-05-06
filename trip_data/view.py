# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import threading
import os
import subprocess
import time

from django.shortcuts import render

from app.models import Spider


def index(request):
    context = {}
    return render(request, 'index.html', context)

def about_me(request):
    context = {}
    return render(request, 'about_me.html', context)

def more_function(request):
    context = {}
    return render(request, 'more_function.html', context)

def page_not_found(request):
    context = {}
    return render(request, '404.html', context)

def spider(request):
    context = {
        'spider':[],
        'date':time.strftime("%Y-%m-%d",time.localtime()),
        'job_name':'',
        'type':1, #1为爬虫 2为数据分析写入mysql
        'action':1,
        'desc':''
    }
    if 'date' in request.GET:
        context['date'] =  request.GET['date']
    if 'job_name' in  request.GET:
        context['job_name'] = request.GET['job_name']
    if 'action' in  request.GET:
        context['action'] = int(request.GET['action']) #1运行 2停止 3设定运行规则（待定）
    if 'type' in request.GET:
        context['type'] = int(request.GET['type'])
    if not context['job_name']:
        pass
    elif context['action'] == 1:
        if context['type'] ==1:
            Spider.objects.filter(reserve_col_1=context['job_name']).update(reserve_col_3=2)
        else:
            Spider.objects.filter(reserve_col_2=context['job_name']).update(reserve_col_3=2)
    else:
        context['desc'] = '暂未开发'
    for item in Spider.objects.all():
        context['spider'].append(item)
    return render(request, 'spider.html', context)