
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect ,render_to_response
from homepage.models import SliderImages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import django.contrib.auth as django_auth
from django.http import HttpResponse
import json



# Create your views here.

def home(request):
    currentUser = request.user

    # 로그인 된 유저인지 확인
    if currentUser.is_authenticated():
        user_role = currentUser.userprofile.role
    else :
        user_role = 0

    # 사용자에 맞는 이미지 가지고오기
    try:
        imgList = SliderImages.objects.filter(role=user_role)
        sendSliderImgs = []
        for t in imgList:
            if t.isAppear == True:
                sendSliderImgs.insert(0, t.imgPath)
    except ObjectDoesNotExist:
        imgList = SliderImages.objects.all()
        sendSliderImgs = []
        for t in imgList:
            if t.isAppear == True:
                sendSliderImgs.insert(0, t.imgPath)

    # 사용자에 맞는 메뉴 수와 이름 가지고 오기
        #TODO: 메뉴 사용자에 맞게 나타나게 고치기
    menu = [
        ('Home', '#'),
        ('Profile', '#'),
        ('Messages', '#'),
        ('(dev) ID : attocube / PW : attocube', '#'),
    ]

    # 메뉴바 오른쪽 부분
        #TODO : 사용자에 맞게 메뉴바 오른쪽 부분도 수정하기
    menu_right = []
    if user_role == 0:
        menu_right = [
            ("로그인", "location.href='/login'"),
            ("회원 가입", "location.href='/signup'"),
        ]
    else:
        menu_right = [
            (currentUser.get_full_name, "location.href='/#'"),
            ("로그 아웃", "location.href='/logout'"),
        ]

    # login check
    if currentUser.is_authenticated():
        if currentUser.userprofile.role == 0:
            return render(request, 'userTemplate/customerTemplate.html',
                          {'imgs':  sendSliderImgs, 'menu': menu, 'menu_right': menu_right, })

        elif currentUser.userprofile.role == 1:
            return render(request, 'userTemplate/teacherTemplate.html',
                          {'imgs':  sendSliderImgs, 'menu': menu, 'menu_right': menu_right, })

        elif currentUser.userprofile.role == 2:
            return render(request, 'userTemplate/investorTemplate.html',
                          {'imgs': sendSliderImgs, 'menu': menu, 'menu_right': menu_right, })
        else:
            return HttpResponse('user role Error')
    else:
        return render(request, 'userTemplate/default_template.html',
                      {'imgs':  sendSliderImgs, 'menu': menu, 'menu_right': menu_right, })


def signup(request):
	return render(request, 'registration/signup.html')

def inputsign(request):

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
    django_auth.logout(request)
    return redirect('/home')

def checkid(request):

    print request.is_ajax()

    ID=request.POST.get('id')

    temp = User.objects.filter(username=ID)

    if temp.exists():
        reval= 0
    else:
        reval= 1

    print request.is_ajax()

    return HttpResponse(json.dumps({'reval': reval}), content_type="application/json")

def logout(request):
    django_auth.logout(request)
    return redirect('/home')

