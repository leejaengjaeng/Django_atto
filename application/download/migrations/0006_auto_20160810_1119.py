# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 02:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('download', '0005_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='commentImages')),
                ('content', models.TextField()),
                ('makeTime', models.DateTimeField(blank=True, null=True)),
                ('delPw', models.CharField(default='0000', max_length=4)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\uac8c\uc2dc\ud310 \ub313\uae00',
                'verbose_name_plural': '\uac8c\uc2dc\ud310 \ub313\uae00',
            },
        ),
        migrations.CreateModel(
            name='CommunityPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='communityImages')),
                ('content', models.TextField()),
                ('headLine', models.TextField()),
                ('makeTime', models.DateTimeField(blank=True, null=True)),
                ('delPw', models.CharField(default='0000', max_length=4)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\uac8c\uc2dc\ud310 \uae00',
                'verbose_name_plural': '\uac8c\uc2dc\ud310 \uae00',
            },
        ),
        migrations.AddField(
            model_name='communitycomment',
            name='connetedPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='download.CommunityPost'),
        ),
    ]
