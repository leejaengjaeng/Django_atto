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

	url(r'^itembasket$',views.itembasket,name='itembasket'),
	url(r'^removebasketitem$',views.removebasketitem,name='removebasketitem'),

	url(r'^addShoppingBasket$', views.addShopingBasket, name='addShopingBasket'),
	url(r'^paypage$',views.paypage,name='paypage'),
	url(r'^payresult$',views.payresult,name='payresult'),
	url(r'^directBuy$',views.directBuy,name='directBuy'),
	url(r'^paypagedirect$',views.paypagedirect,name='paypagedirect')
]

