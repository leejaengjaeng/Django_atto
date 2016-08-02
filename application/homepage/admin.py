from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import userProfile, SliderImages
# Register your models here.

class userProfileInline(admin.StackedInline):
    model = userProfile
    can_delete = True
    verbose_name_plural = 'User_Profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (userProfileInline,)

class SliderImagesAdmin(admin.ModelAdmin):
    list_display = ('imgName', 'isAppear', 'role')

# Re register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(SliderImages, SliderImagesAdmin)
