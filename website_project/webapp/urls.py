from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from webapp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accessrecords/', views.accrec, name='accrec')
]
