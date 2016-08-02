# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def qa(request):
    email = ""
    username = ""
    name = ""
    tel = ""

    if request.user.is_active :
        email = request.user.email
        username = request.user.username
        name = request.user.first_name
        tel = request.user.userprofile.mobilePhoneNumber

    context = {
        'email':email,
        'username' : username,
        'name' : name,
        'tel': tel
    }
    return render(request, "qa/qa.html", context)

def oneqa(request):
    import json

    email = request.GET.get('email', None)
    username = request.GET.get('username', None)
    name = request.GET.get('name', None)
    tel = request.GET.get('tel', None)
    query = request.GET.get('query', None)

    users = User.objects

    if users.filter(username=username).exists():
        user = users.filter(username=username).get()
        user.email = email
        user.first_name = name
        user.userprofile.mobilePhoneNumber = tel
        user.userprofile.save()
        user.save()

        qna = QnA.objects.create(user=user, query=query)
    else :
        result = {'success': False}
        return HttpResponse(json.dumps(result))

    result = {'success' : True}
    return HttpResponse(json.dumps(result))