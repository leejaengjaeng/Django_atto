# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='delPw',
            field=models.CharField(default='0000', max_length=4),
        ),
    ]
