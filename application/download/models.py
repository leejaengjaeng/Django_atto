# encoding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.
class singcontents(models.Model):
    file=models.FileField(upload_to='singcontents')
    text=models.TextField(default="")
    source=models.URLField(max_length=300)

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = '동요 자료'
        verbose_name_plural = '동요 다운로드'

class doccontents(models.Model):
    file=models.FileField(upload_to='docucontents')
    text=models.TextField(default="")
    docuimg=models.ImageField(upload_to='docuimg')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = '교육 가이드'
        verbose_name_plural = '교육 가이드 다운로드'

class CommunityPost(models.Model):
    author = models.ForeignKey(User,unique=False,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='communityImages')
    content = models.TextField(null=False)
    headLine = models.TextField(null=False)
    makeTime = models.DateTimeField(blank=True, null=True)
    delPw = models.CharField(max_length=4, default='0000')
    hit = models.PositiveIntegerField(default=0)
    isNotify = models.BooleanField(default=False)

    def __unicode__(self):
        return self.headLine

    class Meta:
        verbose_name = '게시판 글'
        verbose_name_plural = '게시판 글'

@receiver(pre_delete, sender=CommunityPost)
def CommunityPost_delete(sender, instance, **kwargs):
	instance.image.delete(False)

class CommunityComment(models.Model):
    author = models.ForeignKey(User,unique=False,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='commentImages')
    content = models.TextField(null=False)
    makeTime = models.DateTimeField(blank=True, null=True)
    delPw = models.CharField(max_length=4, default='0000')
    connetedPost = models.ForeignKey(CommunityPost,unique=False,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '게시판 댓글'
        verbose_name_plural = '게시판 댓글'

@receiver(pre_delete, sender=CommunityComment)
def CommunityComment_delete(sender, instance, **kwargs):
    instance.image.delete(False)
