# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import ShopItem, Review, pay
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
import json
import application.common.customUserHandler as cuh

from django.utils.datastructures import MultiValueDictKeyError
from django.core import serializers

# Create your views here.
def itemDetail(request):
    itemId = request.GET.get('itemId')
    try:
        item = ShopItem.objects.get(id=itemId)
        print item.detailImage
    except:
        item = None

    return render(request, "store/item_detail.html", {'item':item})

def shop(request):
    items = ShopItem.objects.all()
    return render(request, "store/shop.html", {'items':items})

def getReviews(request):
    reviews = cuh.getReviews(request)
    return HttpResponse(json.dumps({'reviews':reviews}), content_type="application/json")


def addReview(request):
    author = User.objects.get(id=request.user.id)
    content = request.POST.get("reviewContent")
    makeTime = datetime.now()
    item = ShopItem.objects.get(id=request.POST.get("itemId"))

    try:
        image = request.FILES['uploadReviewImg']
    except MultiValueDictKeyError:
        image = None;

    newReview = Review(author=author, content=content, makeTime=makeTime, itemNum=item, image=image)
    newReview.save()
    return redirect('/shop/detail?itemId='+str(item.id))

def addShopingBasket(request):
    itemId = request.POST.get('itemId')
    item = ShopItem.objects.get(id=itemId)
    count=0
    if item.detailImage:
        detailImg = item.detailImage.url
    else:
        detailImg = None

    if item.image:
        itemImg = item.image.url;
    else :
        itemImg = None;

    inputValue = [itemImg,detailImg,item.itemName,item.price,item.stock,item.sale,item.category,item.info]


    if 'shopingBasket' in request.session:
        sessionList = request.session['shopingBasket']
        print sessionList
        sessionList.append(inputValue)
        print sessionList
        request.session['shopingBasket'] = sessionList

        #request.session['shopingBasket'].append(inputValue)
    else:
        input = []
        input.append(inputValue)
        print input
        request.session['shopingBasket'] = input

    print request.session['shopingBasket']
    return HttpResponse()

def itembasket(request):
    if(request.user.is_authenticated()):
        if 'shopingBasket' in request.session:
            totalprice=0
            saleprice=0
            resultprice=0
            for k in request.session['shopingBasket']:
                totalprice=totalprice+k[3]
                saleprice=saleprice+k[5]
                resultprice=resultprice+(k[3]-k[5])
            return render(request,"store/item_basket.html",{"itemlist":request.session['shopingBasket'],'totalp':totalprice,'salep':saleprice,'resultp':resultprice})
        else:
            return render(request,"store/item_basket.html")

    else:
        return render(request,"userTemplate/loginPage.html")

def removebasketitem(request):
    count=request.POST.get('number')
    n=int(count)
    print count
    list= request.session['shopingBasket']
    print list[n]
    list.pop(n)
    print list
    request.session['shopingBasket']=list
    return redirect('/shop/itembasket')

def paypage(request):
    curuser=request.user
    num=request.user.userprofile.mobilePhoneNumber
    num1=num[0]+num[1]+num[2]
    num2=num[3]+num[4]+num[5]+num[6]
    num3=num[7]+num[8]+num[9]+num[10]
    addrdetail1=curuser.userprofile.address_line2.split(')')[0]+')'
    addrdetail2=curuser.userprofile.address_line2.split(')')[1]
    print addrdetail1
    totalprice = 0
    saleprice = 0
    resultprice = 0
    for k in request.session['shopingBasket']:
        totalprice = totalprice + k[3]
        saleprice = saleprice + k[5]
        resultprice = resultprice + (k[3] - k[5])
    return render(request,"store/pay.html",
                  {"userprofile":curuser.userprofile,"user":curuser,"num1":num1,"num2":num2,"num3":num3,"addrdetail1":addrdetail1,"addrdetail2":addrdetail2,
                   "itemlist": request.session['shopingBasket'], 'totalp': totalprice, 'salep': saleprice,
                   'resultp': resultprice})



def payresult(request):
    name=request.POST.get("rename")
    phone=request.POST.get("renum1")+request.POST.get("renum2")+request.POST.get("renum3")
    addr=request.POST.get("addr1")+' '+request.POST.get("addr2")
    phone2=request.POST.get("phone2")
    require=request.POST.get("require")
    howToPay=request.POST.get("howToPay")
    cost=request.POST.get("cost")
    itemlist=[]
    for k in request.session['shopingBasket']:
        itemlist.append(k[2])
    userid=request.user.username
    print userid
    pay.objects.create(userid=request.user,
                                receivername = name,
                                receiverphonenumber = phone,
                                receiveraddress = addr,
                                receiverphonenumber2 = phone2,
                                itemlist = itemlist,cost = cost,
                                require=require,
                                ispay = False,
                                isreceive = False,
                                howToPay=howToPay)

    return redirect('/shop/paypage')