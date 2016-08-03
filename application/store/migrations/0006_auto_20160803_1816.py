# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 09:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20160803_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='itemNum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ShopItem'),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='sale',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
