# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 02:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160319_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 19, 2, 21, 12, 485020, tzinfo=utc)),
        ),
    ]
