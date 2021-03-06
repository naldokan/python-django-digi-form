# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 05:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_explorer', '0006_auto_20160503_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='JusticeOfPeace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('jp_number', models.CharField(blank=True, max_length=32)),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('mobile_number', models.CharField(blank=True, max_length=24, verbose_name='Contact Number')),
                ('phone', models.CharField(blank=True, max_length=24, verbose_name='Contact Number')),
                ('phone2', models.CharField(blank=True, help_text='After hour', max_length=24, verbose_name='Contact Number2')),
                ('state', models.CharField(blank=True, max_length=24, verbose_name='State')),
                ('raw', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
