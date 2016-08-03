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
	detailImage = models.ImageField(upload_to='shopItemImgs/detail', blank=True)
	itemName = models.CharField(max_length=100)
	price = models.PositiveSmallIntegerField(default=0)
	stock = models.PositiveSmallIntegerField(default=0)
	sale = models.PositiveSmallIntegerField(default=0)

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
    author = models.ForeignKey(User)
    image = models.ImageField(upload_to='shopItemImgs/item')
    content = models.TextField(null=False)
    makeTime = models.DateTimeField(auto_now=True)
    itemNum = models.ForeignKey(ShopItem)

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '상품 댓글'
        verbose_name_plural = '상품 댓글들 '
