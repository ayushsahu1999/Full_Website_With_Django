from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from webapp import views

# Template tagging
app_name = 'webapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accessrecords/', views.AccRecListView.as_view(), name='accrec'),
    url(r'^register/', views.form_name_view, name='register'),
    url(r'^users/', views.UsersCreateView.as_view(), name='users'),
    url(r'^users_list/$', views.UsersListView.as_view(), name='userlist'),
    url(r'^users_list/(?P<pk>\d+)/$', views.UsersDetailView.as_view(), name='userdetail'),
    url(r'^update/(?P<pk>\d+)/$', views.UsersUpdateView.as_view(), name='userupdate'),
    url(r'^delete/(?P<pk>\d+)/$', views.UsersDeleteView.as_view(), name='userdelete'),
    url(r'^login/$', views.user_login, name='user_login')
]
