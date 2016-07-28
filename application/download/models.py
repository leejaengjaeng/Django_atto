# encoding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class singcontents(models.Model):
    video=models.FileField(upload_to='singcontents')
    text=models.TextField(default="")
    source=models.URLField(max_length=300)

    def __str__(self):
        return self.video.name