from django.shortcuts import render,redirect,render_to_response
from homepage.models import SliderImages
from django.contrib.auth.models import User
from django.http import HttpResponse

import django.contrib.auth as djangoAuth


# Create your views here.

def home(request):
	imgList = SliderImages.objects.all()
	sendToTemplate =[]
	for t in imgList:
		if t.isAppear==True : 
			sendToTemplate.insert(0,t.imgPath)

	#login check
	if request.user.is_authenticated():
		# TODO : changing by role
		return render(request,'userTemplate/logged_in.html',{'imgs':sendToTemplate,'user':request.user.get_full_name})
	else :
		return render(request,'userTemplate/default_template.html',{'imgs':sendToTemplate})

def signup(request):
    if (request.method == 'GET'):
        ID = request.GET.get('id')
        temp = User.objects.filter(username=ID)
        response_data = {}
        if temp.exists():
            # reval = "0"
            response_data['result'] = '0'
        else:
            # reval = "1"
            response_data['result'] = '1'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
	return render(request, 'registration/signup.html')

def inputsign(request):
    if(request.method=='GET'):
        ID = request.GET.get('id')
        temp = User.objects.filter(username=ID)
        response_data = {}
        if temp.exists():
            #reval = "0"
            response_data['result']='0'
        else:
            #reval = "1"
            response_data['result'] = '1'
        return HttpResponse(json.dumps(response_data),content_type="application/json")
        #return HttpResponse('<h1>page was sss</h1>')
    name = request.POST.get("name", str)
    username = request.POST.get("id", str)
    pwd = request.POST.get("pwd", str)
    email1 = request.POST.get("email1", str)
    email2 = request.POST.get("email2", str)
    addr1=request.POST.get("addr1",str)
    addr2 = request.POST.get("addr2", str)
    addr3 = request.POST.get("addr3", str)
    repwd = request.POST.get("repwd", str)
    role = request.POST.get("major", str)
    mPhoneNum = request.POST.get("phonenum", str)
    user = User.objects.create_user(username=username,email=email1+"@"+email2,password=pwd,last_name=name)
    user.userprofile.mobilePhoneNumber=mPhoneNum
    user.userprofile.address_line1=addr1
    user.userprofile.address_line2=addr2+" "+addr3
    user.userprofile.role=role
    user.userprofile.save()
    return redirect('/home')

def logout(request):
	djangoAuth.logout(request)
	return redirect('/home')

import json

def checkIDv(request):
    ID=request.GET.get('id')
    temp = User.objects.filter(username=ID)
    reval={}
    if temp.exists():
        reval["exist"]="0"

    else:
        reval["exist"]="1"

    return HttpResponse(json.dumps(reval),content_type="application/json")
