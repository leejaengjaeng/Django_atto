from __future__ import unicode_literals

from django.db import models

# Create your models here.
class singcontents(models.Model):
    video=models.FileField(upload_to='singcontents')
    text=models.CharField(max_length=200)
    source=models.URLField(max_length=300)