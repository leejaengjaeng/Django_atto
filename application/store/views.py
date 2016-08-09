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
    content = request.POST.get("reviewModalContent")
    delPw = request.POST.get("reviewDelPw")
    makeTime = datetime.now()
    item = ShopItem.objects.get(id=request.POST.get("itemId"))

    try:
        image = request.FILES['uploadReviewImg']
    except MultiValueDictKeyError:
        image = None;

    newReview = Review(author=author, content=content, makeTime=makeTime, itemNum=item, image=image, delPw=delPw)
    newReview.save()
    return redirect('/shop/detail?itemId='+str(item.id))

def delReview(request):
    id = request.POST.get("id")
    inputPw = request.POST.get("pw",str).encode("utf-8")
    review = Review.objects.get(id=id)

    print inputPw
    print review.delPw

    if inputPw == review.delPw:
        review.delete()
        retVal = 1
    else:
        retVal = 0

    return HttpResponse(retVal)


def addShopingBasket(request):
    itemId = request.POST.get('itemId')
    itemQuantity = int(request.POST.get('itemQuantity'))

    item = ShopItem.objects.get(id=itemId)

    if item.detailImage:
        detailImg = item.detailImage.url
    else:
        detailImg = None

    if item.image:
        itemImg = item.image.url;
    else :
        itemImg = None;

    inputValue = [itemImg,detailImg,item.itemName,item.price,item.stock,item.sale,item.category,item.info,itemQuantity,itemId]


    if 'shopingBasket' in request.session:
        sessionList = request.session['shopingBasket']

        # for k in request.session['shopingBasket']:
        for k in sessionList:
            if k[9]==inputValue[9]:
                k[8]=k[8]+inputValue[8]
                request.session['shopingBasket'] = sessionList

                print request.session['shopingBasket']
                return HttpResponse()

        #print sessionList
        sessionList.append(inputValue)
        print sessionList
        request.session['shopingBasket'] = sessionList

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
                totalprice=totalprice+k[3]*int(k[8])
                saleprice=saleprice+k[5]*int(k[8])
                resultprice=resultprice+(k[3]*int(k[8])-k[5]*int(k[8]))
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
    addrdetail1=curuser.userprofile.address_line1
    addrdetail2=curuser.userprofile.address_line2
    addrdetail3=curuser.userprofile.address_line3

    totalprice = 0
    saleprice = 0
    resultprice = 0

    for k in request.session['shopingBasket']:
        totalprice = totalprice + k[3] * int(k[8])
        saleprice = saleprice + k[5] * int(k[8])
        resultprice = resultprice + (k[3] * int(k[8]) - k[5] * int(k[8]))
    return render(request,"store/pay.html",
                  {"userprofile":curuser.userprofile,"user":curuser,"num":num,"addrdetail1":addrdetail1,"addrdetail2":addrdetail2,"addrdetail3":addrdetail3,
                   "itemlist": request.session['shopingBasket'], 'totalp': totalprice, 'salep': saleprice,
                   'resultp': resultprice})

def payresult(request):
    name=request.POST.get("rename")
    phone=request.POST.get("renum")
    addr=request.POST.get("addr1")+' '+request.POST.get("addr2")+' '+request.POST.get("addr3")
    phone2=request.POST.get("phone2")
    require=request.POST.get("require")
    howToPay=request.POST.get("howToPay")
    cost=request.POST.get("cost")
    isBasket=request.POST.get("sessionobj")
    print isBasket
    itemlist=''
    count='ea'
    if(isBasket=="0"):
        itemlist=request.session['directBuy'][0][2]+' 1ea'
    else:
        for k in request.session['shopingBasket']:
            itemlist=itemlist+k[2]+' '+str(k[8])+count+'\n'

    userid=request.user.username

    pay.objects.create(userid=request.user,
                                receivername = name,
                                receiverphonenumber = phone,
                                receiveraddress = addr,
                                receiverphonenumber2 = phone2,
                                itemlist = itemlist,
                                cost = cost,
                                require=require,
                                ispay = False,
                                isreceive = False,
                                howToPay=howToPay)

    return redirect('/shop/paypage')

def directBuy(request):
    itemId = request.POST.get('itemId')
    itemQuantity = int(request.POST.get('itemQuantity'))

    item = ShopItem.objects.get(id=itemId)

    if item.detailImage:
        detailImg = item.detailImage.url
    else:
        detailImg = None

    if item.image:
        itemImg = item.image.url;
    else:
        itemImg = None;

    inputValue = [itemImg, detailImg, item.itemName, item.price, item.stock, item.sale, item.category, item.info,
                  0, itemId]


    input = []
    input.append(inputValue)
    print input
    request.session['directBuy'] = input

    print request.session['directBuy'][0][8]
    return HttpResponse()

def paypagedirect(request):

    curuser=request.user
    num=request.user.userprofile.mobilePhoneNumber
    addrdetail1=curuser.userprofile.address_line1
    addrdetail2=curuser.userprofile.address_line2
    addrdetail3=curuser.userprofile.address_line3

    totalprice = 0
    saleprice = 0
    resultprice = 0


    totalprice = request.session['directBuy'][0][3]
    saleprice = request.session['directBuy'][0][5]
    resultprice = totalprice-saleprice
    return render(request,"store/pay.html",
                  {"userprofile":curuser.userprofile,"user":curuser,"num":num,"addrdetail1":addrdetail1,"addrdetail2":addrdetail2,"addrdetail3":addrdetail3,
                   "itemlist": request.session['directBuy'], 'totalp': totalprice, 'salep': saleprice,
                   'resultp': resultprice})