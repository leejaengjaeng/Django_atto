# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

# base
urlpatterns = [
	url(r'^$', views.index, name='index'),
]

