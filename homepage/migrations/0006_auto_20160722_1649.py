# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_sliderimages_imgname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', django_thumbs.db.models.ImageWithThumbsField(upload_to='images')),
                ('second_photo', django_thumbs.db.models.ImageWithThumbsField(upload_to='images')),
            ],
        ),
        migrations.AlterModelOptions(
            name='sliderimages',
            options={},
        ),
    ]
