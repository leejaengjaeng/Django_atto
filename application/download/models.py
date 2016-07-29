# encoding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class singcontents(models.Model):
    file=models.FileField(upload_to='singcontents')
    text=models.TextField(default="")
    source=models.URLField(max_length=300)

    def __str__(self):
        return self.file.name

class doccontents(models.Model):
    file=models.FileField(upload_to='docucontents')
    text=models.TextField(default="")
    docuimg=models.ImageField(upload_to='docuimg')

    def __str__(self):
        return self.file.name