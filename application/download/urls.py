# -*- coding: utf-8 -*-
from django.conf.urls import url
import django.contrib.auth.views as auth_views
from . import views

# base
urlpatterns = [
	url(r'^$',views.delThis, name='delThis'),
	url(r'^downcontents/',views.downcontents ,name='downcontents'),
	url(r'^downdocs/',views.downdocs,name='downdocs')
]

