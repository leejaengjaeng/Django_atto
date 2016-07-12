from django.shortcuts import render,redirect
from homepage.models import SliderImages

from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def home(request):
	imgList = SliderImages.objects.all()
	sendToTemplate =[]
	for t in imgList:
		if t.isAppear==True : 
			sendToTemplate.insert(0,t.imgPath)
	return render(request,'homepage/attocube_main.html',{'imgs':sendToTemplate})

def signup(request):
	return render(request, 'registration/signup.html')

def inputsign(request):
	name = request.POST.get("name", str)
	username = request.POST.get("id", str)
	pwd = request.POST.get("pwd", str)
	repwd = request.POST.get("repwd", str)
	groups = request.POST.get("major", str)
	mPhoneNum = request.POST.get("phonenum", str)
	teleNum = request.POST.get("telenum",str)
	user = User.objects.create_user(username=username, email=None, password=pwd,last_name=name)
	user.userprofile.mobilePhoneNumber=mPhoneNum
	user.userprofile.phoneNumber=teleNum
	user.userprofile.save()
	return redirect('/home')
	#	render(request,'homepage/attocube_main.html')
#	return render(request, 'registration/signup.html')

def index(request):
	return HttpResponse("Hello<br>This page will be the attocube's homepage")

def index2(request):
	return HttpResponse("SecondPage")

def imgTest(request):
	imgList = SliderImages.objects.all()
	sendToTemplate =[]
	for t in imgList:
		if t.isAppear==True : 
			sendToTemplate.insert(0,t.imgPath)
	print sendToTemplate

	return render(request,'homepage/imgTest.html',{'cnt':1,'imgs': sendToTemplate})

def Test(request):
	a = request.GET.get("username", None)
	b = request.GET.get("email", None)
	c = request.GET.get("password", None)
	return HttpResponse(a + "/" + b + "/" + c)