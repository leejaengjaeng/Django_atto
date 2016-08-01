from django.contrib import admin
from application.download.models import singcontents
from application.download.models import doccontents
# Register your models here.
admin.site.register(singcontents)
admin.site.register(doccontents)