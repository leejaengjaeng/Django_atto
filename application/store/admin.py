from django.contrib import admin

# Register your models here.
from .models import ShopItem,Review

#class ItemReviews(Review):
#    list_display = ('author','makeTime', 'image', 'content','itemNum')


#admin.site.register(ItemReviews)
admin.site.register(ShopItem)

admin.site.register(Review)
