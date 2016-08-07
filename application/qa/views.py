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
        name = request.user.get_full_name()
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
    from datetime import datetime

    username = request.GET.get('username', None)
    query = request.GET.get('query', None)

    users = User.objects

    if users.filter(username=username).exists():
        user = users.filter(username=username).get()
        QnA.objects.create(user=user, query=query, time=datetime.now())
        from django.core.mail import send_mail

        send_mail(
            subject=u'[문의사항]',
            message=query,
            from_email='attocube@attocube.co.kr',
            recipient_list=['contactus@attocube.co.kr'],
            fail_silently=False
        )
    else :
        result = {'success': False}
        return HttpResponse(json.dumps(result))

    result = {'success' : True}
    return HttpResponse(json.dumps(result))