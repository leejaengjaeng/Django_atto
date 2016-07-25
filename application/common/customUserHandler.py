# -*- coding: utf-8 -*-
from application.homepage.models import SliderImages
from django.core.exceptions import ObjectDoesNotExist

#메뉴바 왼쪽 부분
def getMenu(reqeust):
    # 사용자에 맞는 메뉴 수와 이름 가지고 오기
    # TODO: 메뉴 사용자에 맞게 나타나게 고치기
    menu = [
        (u'제품 소개', '/shop'),
        (u'고객 센터', '#'),
        (u'브랜드 소개', '#'),
        (u'콘텐츠', '#'),
        (u'다운로드', '#'),
    ]
    return menu

# 메뉴바 오른쪽 부분
def getMenuRight(request):
    # 로그인 된 유저인지 확인
    currentUser = request.user
    if currentUser.is_authenticated():
        menu_right = [
            (currentUser.get_full_name, "location.href='/myaccount'"),
            ("로그 아웃", "location.href='/logout'"),
        ]
    else:
        menu_right = [
            ("로그인", "location.href='/login'"),
            ("회원 가입", "location.href='/signup'"),
        ]
    return menu_right


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

