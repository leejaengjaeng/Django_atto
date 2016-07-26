# -*- coding: utf-8 -*-
from application.homepage.models import SliderImages, shopItem
from django.core.exceptions import ObjectDoesNotExist
import json

#메뉴바 왼쪽 부분
def setMenuToSession(request):

    # TODO: 메뉴 사용자에 맞게 나타나게 고치기
    menu = []

    menu_right = []
    menu_left = []
    role =0

    if request.user.is_authenticated():
        menu_right = [
            (request.user.get_full_name(), "/myaccount"),
            ("로그 아웃", "/logout"),
        ]
    else:
        menu_right = [
            ("로그인", "/login"),
            ("회원 가입", "/signup"),
        ]


    if role == 0 :
        menu_left = [
            (u'Intro', '#'),
            (u'Q&A', '/qa'),
            (u'Shop', '/shop'),
            (u'Download', '#'),
            (u'제품 후기', '#'),
            (u'디폴트,구매자', '#'),
        ]
    else :
        menu_left = [
            (u'Intro', '#'),
            (u'Q&A', '/qa'),
            (u'Shop', '/shop'),
            (u'Download', '#'),
            (u'제품 후기', '#'),
        ]

    request.session['nav_left'] = menu_left
    request.session['nav_right'] = menu_right
    return


# 사용자에 맞는 이미지 가지고오기
def getSliderImages(request):
    if request.user.is_authenticated():
        user_role =request.user.userprofile.role
    else:
        user_role = 0

    sendSliderImgs = []
    try:
        imgList = SliderImages.objects.filter(role=user_role)
        for t in imgList:
            if t.isAppear == True:
                sendSliderImgs.insert(0, t)
    except ObjectDoesNotExist:
        imgList = SliderImages.objects.all()
        for t in imgList:
            if t.isAppear == True:
                sendSliderImgs.insert(0, t)

    return sendSliderImgs

def getItemList(request):
    itemList =[]
    try:
        itemList = shopItem.objects.all()
    #TODO:나타낼 상품이 하나도 없는 경우, 어떻게 할지 결정하기
    except ObjectDoesNotExist:
        itemList = []
    return itemList

