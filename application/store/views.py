from django.shortcuts import render
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