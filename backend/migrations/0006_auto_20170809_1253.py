# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20170808_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=16, unique=True),
        ),
    ]
