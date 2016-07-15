from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class SliderImages(models.Model):
	imgId = models.AutoField(primary_key=True)
	imgPath = models.CharField(max_length=256)
	isAppear = models.BooleanField(default=True)
	imgName = models.CharField(max_length=100)
	role = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.imgName
	#registDate = models.DateField.auto_now
	#expireDate = models.DateField

class userProfile(models.Model):
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			userProfile.objects.create(user=instance)
#		else:
			# update
#			if User.userprofile:
#				User.userprofile.save()


	user = models.OneToOneField(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE, parent_link=True, primary_key=True)
	#user.username is id and, first_name/ last_name is real name
	address_line1 = models.CharField(max_length=100,null=True)
	address_line2 = models.CharField(max_length=100,null=True)
	mobilePhoneNumber = models.CharField(max_length=50,null=True)
	phoneNumber = models.CharField(max_length=50,null=True)
	role = models.PositiveSmallIntegerField(default=0, null=False)
	post_save.connect(create_user_profile, sender=User)

	def __str__(self):
			return self.user.username
