# -*- coding: utf-8 -*-
from django.conf.urls import url
import django.contrib.auth.views as auth_views
from . import views

# base
urlpatterns = [
	url(r'^$',views.news, name='news'),
	url(r'^detail$', views.newsDetail, name='newsDetail'),
	url(r'^getComments$', views.showComments, name='showComments'),
	url(r'^addComment$', views.addComment, name='addComment'),

]

