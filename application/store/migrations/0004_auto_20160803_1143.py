# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20160803_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='itemNum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ShopItem'),
        ),
    ]
