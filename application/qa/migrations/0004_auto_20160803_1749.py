# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_auto_20160803_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='time',
            field=models.DateTimeField(default=''),
        ),
    ]
