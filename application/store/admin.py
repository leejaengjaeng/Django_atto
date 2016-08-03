from django.contrib import admin

# Register your models here.
from .models import ShopItem,Review

admin.site.register(ShopItem)
admin.site.register(Review)
