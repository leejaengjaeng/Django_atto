# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimages',
            name='isAppear',
            field=models.BooleanField(default=True),
        ),
    ]
