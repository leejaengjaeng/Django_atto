from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QnA(models.Model):
    user = models.ForeignKey(User, unique=False)
    query = models.TextField(default="")
    time = models.DateTimeField(blank=True, null=True)
    check = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

