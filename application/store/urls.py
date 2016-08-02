# -*- coding: utf-8 -*-
from django.conf.urls import url
import django.contrib.auth.views as auth_views
from . import views

# base
urlpatterns = [
	url(r'^$',views.shop, name='store'),
	url(r'^detail$', views.itemDetail, name='itemDetail'),
	url(r'^addReview$', views.addReview, name='addReview'),
	url(r'^getReviews$', views.getReviews, name='getReviews'),
]

