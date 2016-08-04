# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20160803_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='itemNum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ShopItem'),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='detailImage',
            field=models.ImageField(upload_to='shopItemImgs/detail'),
        ),
    ]