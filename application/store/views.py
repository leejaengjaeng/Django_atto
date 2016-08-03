from django.shortcuts import render,redirect
from models import ShopItem,Review
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
import json
import application.common.customUserHandler as cuh

from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def itemDetail(request):
    itemId = request.GET.get('itemId')
    try:
        item = ShopItem.objects.get(id=itemId)
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
    print content
    item = ShopItem.objects.get(id=request.POST.get("itemId"))

    try:
        image = request.FILES['uploadReviewImg']
    except MultiValueDictKeyError:
        image = None;

    newReview = Review(author=author, content=content, makeTime=makeTime, itemNum=item, image=image)
    newReview.save()

    return redirect('/shop/detail?itemId='+str(item.id))