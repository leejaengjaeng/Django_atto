# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    image = models.ImageField(upload_to='newsImages', default='newsImages/default.jpg')
    headLine = models.CharField(max_length=100, null=False)
    contentsImg = models.ImageField(upload_to='newsImages', blank=True)
    contentsLink = models.CharField(max_length=200, blank=True, verbose_name='기사면 링크 주소, 아니라면 빈칸')
    makeTime = models.DateTimeField(auto_now_add=True)
    modifyTime = models.DateTimeField(auto_now=True)
    #author = models.CharField(max_length=50,null=False)
    author = models.ForeignKey(User)
    hits = models.PositiveIntegerField(default=0)
    commentsCnt = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return self.headLine

    class Meta:
        verbose_name = '홍보 소식'
        verbose_name_plural = '홍보 소식들'

class Comments(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField(null=False)
    makeTime = models.DateTimeField(auto_now=True)
    postNum = models.ForeignKey(Posts)
    delPw = models.CharField(max_length=4,default='0000')

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '홍보 소식 댓글'
        verbose_name_plural = '홍보 소식 댓글들 '
