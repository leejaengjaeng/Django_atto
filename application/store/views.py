from django.shortcuts import render,redirect
from models import ShopItem,Review
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

        return render(request,"store/item_basket.html",{"itemlist":request.session['shopingBasket']})
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
