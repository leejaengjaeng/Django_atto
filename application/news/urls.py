# -*- coding: utf-8 -*-
from django.conf.urls import url
import django.contrib.auth.views as auth_views
from . import views

# base
urlpatterns = [
	url(r'^$',views.news, name='news'),
]

