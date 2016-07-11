from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SliderImages(models.Model):
	imgId = models.AutoField(primary_key=True)
	#imgPath = models.ImageField(upload_to='homepage/') #upload_to seems not working
	imgPath = models.CharField(max_length=256)
	isAppear = models.BooleanField(default=True)
	imgName = models.CharField(max_length=100)
	role = models.PositiveSmallInteger(default=0)
	# 0 : 방문자(언제나 보여줌?), 1:, 2:, :3, ...
 
	def __str__(self):
		return self.imgName
	#registDate = models.DateField.auto_now
	#expireDate = models.DateField
	#imgPath? , model.ImageField(upload_to='.....') #file will be saved to MEDIA_ROOT/.... 

class Users(models.Model):
	autoId = models.AutoField(primary_key=True)
	userId = models.CharField(max_length=50,null=False)
	userpw = models.CharField(max_length=50,null=False)
	name = models.CharField(max_length=100,null=False)
	address_line1 = models.CharField(max_length=100,null=False)
	address_line2 = models.CharField(max_length=100,null=False)
	mobilePhoneNumber = models.CharField(max_length=50,null=False)
	phoneNumber = models.CharField(max_length=50)
	role = models.PositiveSmallInteger(default=0)
	# 0: 방문자 , 1: , 2: ,3: ,...
