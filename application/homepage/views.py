# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect ,render_to_response
from django.contrib.auth.models import User
import django.contrib.auth as django_auth
from django.http import HttpResponse
import json
import application.common.customUserHandler as cuh

# Create your views here.

def home(request):
    request.encoding = 'utf-8'
    currentUser = request.user
    sliderImgs = cuh.getSliderImages(request)

    itemList = cuh.getItemList(request)
    return render(request, 'userTemplate/default_template.html',
                  {'imgs': sliderImgs, 'items': itemList})

    # # 로그인 체크
    # if currentUser.is_authenticated():
    #     if currentUser.userprofile.role == 0:
    #         itemList = cuh.getItemList(request)
    #         return render(request, 'userTemplate/customerTemplate.html',
    #                       {'imgs':  sliderImgs, 'items':itemList})
    #
    #     elif currentUser.userprofile.role == 1:
    #         return render(request, 'userTemplate/teacherTemplate.html',
    #                       {'imgs':  sliderImgs})
    #
    #     elif currentUser.userprofile.role == 2:
    #         return render(request, 'userTemplate/investorTemplate.html',
    #                       {'imgs': sliderImgs})
    #     else: #role이 입력되어있지 않은경우
    #         return HttpResponse('user role Error')
    # else:
    #     itemList = cuh.getItemList(request)
    #     return render(request, 'userTemplate/default_template.html',
    #                   {'imgs':  sliderImgs, 'items':itemList})


def signup(request):
	return render(request, 'registration/signup.html')

def inputsign(request):

    name = request.POST.get("name", str)
    username = request.POST.get("id", str)
    pwd = request.POST.get("pwd", str)
    email1 = request.POST.get("email1", str)
    email2 = request.POST.get("email3", str)
    addr1=request.POST.get("addr1",str)
    addr2 = request.POST.get("addr2", str)
    addr3 = request.POST.get("addr3", str)
    repwd = request.POST.get("repwd", str)
    role = request.POST.get("major", str)
    mPhoneNum = request.POST.get("phonenum", str)
    user = User.objects.create_user(username=username,email=email1+"@"+email2,password=pwd,last_name=name)
    user.userprofile.mobilePhoneNumber=mPhoneNum
    user.userprofile.address_line1=addr1
    user.userprofile.address_line2=addr2
    user.userprofile.address_line3=addr3
    user.userprofile.role=role
    user.userprofile.save()

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

def shop(request):

    sliderImgs = cuh.getSliderImages(request)
    items = cuh.getItemList(request)

    return render(request, 'homepage/shop.html',
                  {'imgs': sliderImgs, 'items':items})

def myaccount(request):
    currentuser = request.user;
    if currentuser.is_authenticated():
        id=currentuser.username
        mail = currentuser.email
        name = currentuser.get_full_name()
        addr1 = currentuser.userprofile.address_line1
        addr2 = currentuser.userprofile.address_line2
        print currentuser.userprofile.address_line3
        addr3= currentuser.userprofile.address_line3
        phonenum = currentuser.userprofile.mobilePhoneNumber
        role = currentuser.userprofile.role
        return render(request,'registration/myaccount.html',
                      {'ids':id,'emails':mail,'names':name,'addr1s':addr1,'addr2s':addr2+" "+addr3,'phonenums':phonenum,'roles':role})


def editaccount(request):
    currentuser=request.user
    if currentuser.is_authenticated():
        id = currentuser.username
        mail = currentuser.email.split('@')
        name = currentuser.last_name
        addr1 = currentuser.userprofile.address_line1
        addr2 = currentuser.userprofile.address_line2
        addr3 = currentuser.userprofile.address_line3
        phonenum = currentuser.userprofile.mobilePhoneNumber
        role = currentuser.userprofile.role
        return render(request, 'registration/editaccount.html',
                      {'ids': id, 'emails': mail, 'names': name, 'addr1s': addr1, 'addr2s': addr2, 'addr3s':addr3,
                       'phonenums': phonenum, 'roles': role})

def editaccountsave(request):
    user=User.objects.get(username=request.user.username)
    newpwd=request.POST.get("pwd");
    user.set_password(newpwd)
    newname=request.POST.get("name");
    user.last_name=newname;
    newemail1= request.POST.get("email1")
    newemail2 = request.POST.get("email2")
    user.email = newemail1+"@"+newemail2
    user.save()
    newphonenum = request.POST.get("phonenum")
    user.userprofile.mobilePhoneNumber=newphonenum
    newaddr1 = request.POST.get("addr1")
    newaddr2 = request.POST.get("addr2")
    newaddr3 = request.POST.get("addr3")
    user.userprofile.address_line1 = newaddr1
    user.userprofile.address_line2 = newaddr2
    user.userprofile.address_line3 = newaddr3
    newrole = request.POST.get("major")
    user.userprofile.role = newrole
    user.userprofile.save()
    return redirect('/home')