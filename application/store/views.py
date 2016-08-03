from django.shortcuts import render,redirect
from models import ShopItem,Review
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
import json

import application.common.customUserHandler as cuh

# Create your views here.
def itemDetail(request):
    itemId = request.GET.get('itemId')
    try:
        item = ShopItem.objects.get(id=itemId)
    except:
        item = None

    return render(request, "store/item_detail.html", {'item':item})

def shop(request):
    return render(request, "store/item_detail.html")

def getReviews(request):
    reviews = cuh.getReviews(request)
    return HttpResponse(json.dumps({'reviews':reviews}), content_type="application/json")

def addReview(request):
    author = User.objects.get(id=request.user.id)
    content = request.POST.get("content", str).encode("utf-8")
    makeTime = datetime.now()
    image = request.POST.get("image")
    itemNum = ShopItem.objects.get(id=request.POST.get("itemNum"))
    newReview = Review(author=author, content=content, makeTime=makeTime, itemNum=itemNum, image=image)
    newReview.save()
    return HttpResponse()

def itembasket(request):
    if(request.user.is_authenticated()):
        curuser=request.user.username

        # request.session[curuser]='data1'
        # a = [{'key' : curuser, 'name1': {'price' : 1000,'deliprice':'deliprice1'},
        #                        'name2':{'price':2000,'deliprice':'deliprice2'},
        #                        'name3':{'price':3000,'deliprice':'deliprice3'}}]
        data = {'name1':{'name':'name1',
                        'price':'price1',
                        'deliprice':'deliprice1'},
              'name2':{'name':'name2',
                       'price':'price2',
                       'deliprice':'deliprice2'},
              'name3':{'name':'name3',
                       'price':'price3',
                       'deliprice':'deliprice3'}}
        request.session[curuser] = data
        basketlist=data
        data1=request.session[curuser]
        return render(request,"store/item_basket.html",{"datas":data1})
    else:
        return render(request,"userTemplate/loginPage.html")

def removebasketitem(request):
    # remove=request.POST.get("remove")
    curuser=request.user.username
    # h=json.load(request.session[curuser])
    # for item in h:
    #     del item[remove]
    return HttpResponse(json.loads(request.session[curuser]))