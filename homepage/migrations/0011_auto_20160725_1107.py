# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20160725_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitem',
            name='itemId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
