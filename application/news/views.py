# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import application.common.customUserHandler as cuh
from models import Posts,Comments
import json
from datetime import datetime
from django.contrib.auth.models import User

from django.template import RequestContext

# Create your views here.
def news(request):
    posts = cuh.getPosts(request)
    return render(request, "news/news.html",{'posts':posts})

def newsDetail(request):
    postId = request.GET.get('newsPost',False)
    try:
        post = Posts.objects.filter(id=postId)[0]
        # 기사인 경우
        if post.contentsLink:
            link = post.contentsLink
        #직접 작성한 글인 경우
        else:
            link = None
        posts = cuh.getPosts(request)
        return render(request, "news/news_detail.html",{'link':link,'post':post})

    except ObjectDoesNotExist:
        #에러 페이지 하나 만들어서 그거 띄우는게 나을것 같슴당
        link = None
        post = None
        return render(request, "news/news_detail.html",{'link':link,'post':post})

def showComments(request):
    comments = cuh.getComments(request)
    print comments

    return HttpResponse(json.dumps({'comments': comments}), content_type="application/json")

def addComment(request):
    author = User.objects.get(id=request.user.id)
    content = request.POST.get("content",str).encode("utf-8")
    makeTime = datetime.now()
    postNum = Posts.objects.get(id=request.POST.get("postNum"))
    delPw = request.POST.get("delPw",str).encode("utf-8")
    newComment = Comments(author=author,content=content,makeTime=makeTime,postNum=postNum,delPw = delPw)
    newComment.save()
    return HttpResponse()

def delComment(request):
    id = request.POST.get("id")
    inputPw = request.POST.get("pw",str).encode("utf-8")
    comment = Comments.objects.get(id=id)

    if inputPw == comment.delPw:
        comment.delete()
        retVal = 1
    else:
        retVal = 0

    return HttpResponse(retVal)

