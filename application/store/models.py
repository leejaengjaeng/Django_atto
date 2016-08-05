# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import post_save, pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ShopItem(models.Model):
	# Setting.py에 있는 MEDIA_ROOT 이후 경로
	image = models.ImageField(upload_to='shopItemImgs/item')
	detailImage = models.ImageField(upload_to='shopItemImgs/detail')
	itemName = models.CharField(max_length=100)
	price = models.PositiveIntegerField(default=0)
	stock = models.PositiveSmallIntegerField(default=0)
	sale = models.PositiveIntegerField(default=0)
	category = models.PositiveSmallIntegerField(default=0)
	info = models.TextField(blank=True)

	class Meta:
		verbose_name = '상품'
		verbose_name_plural = '상품들'

	def __unicode__(self):
		return self.itemName

@receiver(pre_delete, sender=ShopItem)
def shopItem_delete(sender, instance, **kwargs):
	instance.detailImage.delete(False)
	instance.image.delete(False)


class Review(models.Model):
	author = models.ForeignKey(User, unique=False)
	image = models.ImageField(upload_to='shopItemImgs/item')
	content = models.TextField(null=False)
	makeTime = models.DateTimeField(blank=True, null=True)
	itemNum = models.ForeignKey(ShopItem, unique=False)

	def __unicode__(self):
		return self.content

	class Meta:
		verbose_name = '상품 댓글'
		verbose_name_plural = '상품 댓글들 '

class pay(models.Model):
	userid=models.ForeignKey(User,unique=False)
	receivername=models.CharField(null=False,max_length=10)
	receiverphonenumber=models.IntegerField(max_length=30)
	receiveraddress=models.CharField(max_length=100)
	receiverphonenumber2=models.CharField(max_length=100)
	itemlist=models.TextField(max_length=500)
	cost=models.IntegerField()
	require=models.TextField(max_length=100)
	ispay=models.BooleanField(default=False)
	isreceive=models.BooleanField(default=False)
	howToPay=models.CharField(max_length=50)

	def __unicode__(self):
		return self.userid.username

	class Meta:
		verbose_name = '결제건'
		verbose_name_plural = '결제 항목들 '
