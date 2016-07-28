from django.contrib import admin

from .models import Posts, Comments
# Register your models here.


# Re register UserAdmin
admin.site.register(Posts)
admin.site.register(Comments)

