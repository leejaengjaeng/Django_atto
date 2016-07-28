from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    image = models.ImageField(upload_to='newsImages', default='newsImages/default.jpg')
    headLine = models.CharField(max_length=100, null=False)
    contents = models.TextField(null=False)
    contentsLink = models.CharField(max_length=200, null=False)
    makeTime = models.DateTimeField(auto_now_add=True)
    modifyTime = models.DateTimeField(auto_now=True)
    #author = models.CharField(max_length=50,null=False)
    author = models.ForeignKey(User)
    hits = models.PositiveIntegerField(default=0)
    commentsCnt = models.PositiveSmallIntegerField(default=0)

class Coments(models.Model):
    author = models.CharField(max_length=50, null=False)
    passwd = models.CharField(max_length=32, null=False)
    content = models.TextField(null=False)
    makeTime = models.DateTimeField(auto_now=True)
    postNum = models.ForeignKey(Posts)
