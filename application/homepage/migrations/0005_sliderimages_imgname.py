# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 07:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_remove_sliderimages_imgname'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimages',
            name='imgName',
            field=models.CharField(default=datetime.datetime(2016, 7, 20, 7, 49, 54, 583000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
