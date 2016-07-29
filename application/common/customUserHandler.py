# -*- coding: utf-8 -*-
from application.homepage.models import SliderImages, shopItem
from application.news.models import Posts,Comments
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
            (u'Shop',u'제품 소개\n\n', '/shop'),
            (u'Q&A',u'고객 센터\n\n', '/qa'),
            (u'Brand',u'브랜드 소개\n\n', '/brand'),
            (u'Download',u'콘텐츠 \n 다운로드', '/download'),
            (u'Recruit',u'인재 채용\n\n', '/recruit'),
            (u'News',u'홍보 소식\n\n', '/news'),
        ]
    else :
        menu_left = [
            (u'Shop', u'제품 소개\n\n', '/shop'),
            (u'Q&A', u'고객 센터\n\n', '/qa'),
            (u'Brand', u'브랜드 소개\n\n', '/brand'),
            (u'Download', u'콘텐츠 \n 다운로드', '/download'),
            (u'Recruit', u'인재 채용\n\n', '/recruit'),
            (u'News', u'홍보 소식\n\n', '/news'),
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


def getPosts(request):
    posts = []
    try:
        posts = Posts.objects.all()
    except ObjectDoesNotExist:
        posts =[]
        #뭔가 예외처리하기
    return posts
