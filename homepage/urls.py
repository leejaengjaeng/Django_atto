from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.home, name='home'),
	url(r'^home/',views.home ,name='home2'),
	url(r'^second/',views.index2, name='test'),
	url(r'^imgTest/',views.imgTest, name='imgtest'),
	url(r'^Test/',views.Test, name='test'),

	url(r'^signup/',views.signup,name='signup'),
	url(r'^login/',
		'django.contrib.auth.views.login',
		name='userLogin',
		kwargs={ 'template_name':'registration/loginTest.html', }
		),
	url(r'^logout/',
		'django.contrib.auth.views.logout'
		,name='userLogout',
		kwargs={ 'template_name':'homepage/attocube_main.html',}
		),
	url(r'^inputsign',views.inputsign,name='inputsign'),

]

