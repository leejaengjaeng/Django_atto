# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 06:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('makeTime', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\ud64d\ubcf4 \uc18c\uc2dd \ub313\uae00',
                'verbose_name_plural': '\ud64d\ubcf4 \uc18c\uc2dd \ub313\uae00\ub4e4 ',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='newsImages/default.jpg', upload_to='newsImages')),
                ('headLine', models.CharField(max_length=100)),
                ('contentsImg', models.ImageField(blank=True, upload_to='newsImages')),
                ('contentsLink', models.CharField(blank=True, max_length=200, verbose_name='\uae30\uc0ac\uba74 \ub9c1\ud06c \uc8fc\uc18c, \uc544\ub2c8\ub77c\uba74 \ube48\uce78')),
                ('makeTime', models.DateTimeField(auto_now_add=True)),
                ('modifyTime', models.DateTimeField(auto_now=True)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('commentsCnt', models.PositiveSmallIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\ud64d\ubcf4 \uc18c\uc2dd',
                'verbose_name_plural': '\ud64d\ubcf4 \uc18c\uc2dd\ub4e4',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='postNum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Posts'),
        ),
    ]
