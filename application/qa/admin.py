from django.contrib import admin
from .models import *
# Register your models here.

class QnAAdmin(admin.ModelAdmin):
    list_display = ('user', 'query', 'time', 'check')

admin.site.register(QnA, QnAAdmin)