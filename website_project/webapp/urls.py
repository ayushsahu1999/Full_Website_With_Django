from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from webapp import views

# Template tagging
app_name = 'webapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accessrecords/', views.accrec, name='accrec'),
    url(r'^formpage/', views.form_name_view, name='form_name'),
    url(r'^users/', views.users, name='users')
]
