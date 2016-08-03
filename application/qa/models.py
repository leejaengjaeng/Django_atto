from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class QnA(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, parent_link=True)
    query = models.TextField(default="")

