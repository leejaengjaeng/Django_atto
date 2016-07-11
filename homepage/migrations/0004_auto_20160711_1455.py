# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20160708_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('autoId', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.CharField(max_length=50)),
                ('userpw', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(max_length=100)),
                ('mobilePhoneNumber', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('role', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='sliderimages',
            name='role',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
