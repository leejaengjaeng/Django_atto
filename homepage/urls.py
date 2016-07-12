from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.home, name='home'),
	url(r'^home/',views.home ,name='home2'),
	url(r'^second/',views.index2, name='test'),
	url(r'^imgTest/',views.imgTest, name='imgtest'),
	url(r'^Test/',views.Test, name='test'),

	url(r'^signup/',views.signup,name='signup'),
	url(r'^inputsign',views.inputsign,name='inputsign'),
]

