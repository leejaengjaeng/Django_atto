from django.shortcuts import render
from homepage.models import sliderImages

from django.http import HttpResponse

# Create your views here.

def home(request):
	imgList = SliderImages.objects.all()
	sendToTemplate =[]
	for t in imgList:
		if t.isAppear==True : 
			sendToTemplate.insert(0,t.imgPath)
	return render(request,'homepage/attocube_main.html',{'imgs':sendToTemplate})

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

