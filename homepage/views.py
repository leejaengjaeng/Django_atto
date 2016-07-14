from django.shortcuts import render,redirect
from homepage.models import SliderImages
from django.contrib.auth.models import User

import django.contrib.auth as django_auth
# Create your views here.

def home(request):
	imgList = SliderImages.objects.all()
	sendToTemplate =[]
	for t in imgList:
		if t.isAppear==True : 
			sendToTemplate.insert(0,t.imgPath)
	currentUser = request.user
	#login check
	if currentUser.is_authenticated():
		# TODO : changing by role
		if currentUser.userprofile.role == 0:
			return render(request,'userTemplate/customerTemplate.html',{'imgs':sendToTemplate,'user':request.user.get_full_name})
		elif currentUser.userprofile.role == 1:
			return render(request, 'userTemplate/teacherTemplate.html',{'imgs': sendToTemplate, 'user': request.user.get_full_name})
		elif currentUser.userprofile.role == 2:
			return render(request, 'userTemplate/investorTemplate.html', {'imgs': sendToTemplate, 'user': request.user.get_full_name})
		else:
			return render(request, 'userTemplate/logged_in.html', {'imgs': sendToTemplate, 'user': request.user.get_full_name})

	else :
		return render(request,'userTemplate/default_template.html',{'imgs':sendToTemplate})

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

def logout(request):
	django_auth.logout(request)
	return redirect('/home')
