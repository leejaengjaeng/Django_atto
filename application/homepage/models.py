# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch.dispatcher import receiver


# Create your models here.

# TODO; 어드민에 썸네일이 나오도록
# TODO; 업로드한 파일 이름이 imgName 으로 저장되도록

class SliderImages(models.Model):
	image = models.ImageField(upload_to='sliderImages')
	isAppear = models.BooleanField(default=True)
	imgName = models.CharField(max_length=100)
	role = models.PositiveSmallIntegerField(default=0)

	def image_thumb(self):
		if self.image:
			return u'<img src="/media/%s" width="100" height="100" />' % (self.image)
	image_thumb.allow_tags = True

	# registDate = models.DateField.auto_now
	# expireDate = models.DateField
	class Meta:
		verbose_name = '메인 슬라이더 이미지'
		verbose_name_plural = '메인 슬라이더 이미지들'

	def __unicode__(self):
		return self.imgName

@receiver(pre_delete, sender=SliderImages)
def SliderImage_delete(sender, instance, **kwargs):
	instance.image.delete(False)



class userProfile(models.Model):
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			userProfile.objects.create(user=instance)
			#		else:
			# update
			#			if User.userprofile:
			#				User.userprofile.save()

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, parent_link=True, primary_key=True)
	# user.username is id and, first_name/ last_name is real name
	address_line1 = models.CharField(max_length=100, null=True)
	address_line2 = models.CharField(max_length=100, null=True)
	mobilePhoneNumber = models.CharField(max_length=50, null=True)
	phoneNumber = models.CharField(max_length=50, null=True)
	role = models.PositiveSmallIntegerField(default=0, null=False)
	post_save.connect(create_user_profile, sender=User)

	def __str__(self):
		return self.user.username


