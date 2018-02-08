# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-08 16:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zad', '0007_auto_20180208_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 16, 25, 9, 108180)),
        ),
        migrations.AlterField(
            model_name='customerfile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 16, 25, 9, 107524)),
        ),
        migrations.AlterField(
            model_name='customerurl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 16, 25, 9, 106824)),
        ),
        migrations.AlterField(
            model_name='customerurl',
            name='url',
            field=models.TextField(),
        ),
    ]
