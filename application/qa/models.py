from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class QnA(models.Model):
    user = models.ForeignKey(User, unique=False)
    query = models.TextField(default="")
    time = models.DateTimeField(default=datetime.now())
    check = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

