# -*- coding: utf-8 -*-
from django.conf.urls import url
import django.contrib.auth.views as auth_views
from . import views

# base
urlpatterns = [
	url(r'^$',views.home, name='home'),
	url(r'^home/',views.home ,name='home2'),
]

# about User
urlpatterns += [
	url(r'^signup/',views.signup,name='signup'),
	url(r'^inputsign',views.inputsign,name='inputsign'),
	url(r'^login/',
		auth_views.login,
		name='userLogin',
		kwargs={ 'template_name':'userTemplate/loginPage.html', }
		),
	url(r'^logout/',views.logout,name="logout"),
    url(r'^checkid',views.checkid,name="checkid"),
	url(r'^shop', views.shop, name="shop"),
	url(r'^myaccount', views.myaccount,name="myaccount"),
	url(r'^editaccount',views.editaccount,name="editaccount"),
	url(r'^editsave',views.editaccountsave,name="editaccountsave"),

]

