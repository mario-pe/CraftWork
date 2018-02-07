# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-07 16:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zad', '0004_auto_20180207_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerfile',
            name='counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customerfile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 16, 23, 47, 792817)),
        ),
        migrations.AlterField(
            model_name='customerurl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 16, 23, 47, 792028)),
        ),
    ]
