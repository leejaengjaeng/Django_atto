# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20160720_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliderimages',
            name='imgName',
        ),
    ]