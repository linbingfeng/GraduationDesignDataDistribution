"""trip_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import hotel_distribution
from trip_data.view import index
from trip_data.view import about_me
from trip_data.view import more_function
from trip_data.view import spider
from app.views import hot_city
from app.views import city_economic
from trip_data.view import page_not_found
from django.conf.urls import handler404

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hotel_distribution/', hotel_distribution),
    url(r'^index/|^$',index),
    url(r'^hot_city/',hot_city),
    url(r'^about_me/',about_me),
    url(r'^more_function/', more_function),
    url(r'^city_economic/', city_economic),
    url(r'^spider/', spider),
]
handler404 = page_not_found
