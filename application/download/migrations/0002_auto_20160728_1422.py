# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singcontents',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
