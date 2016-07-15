# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 08:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('homepage', '0005_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(max_length=100)),
                ('mobilePhoneNumber', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]