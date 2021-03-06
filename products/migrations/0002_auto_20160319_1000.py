# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 02:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 19, 2, 0, 7, 22814, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='product',
            name='valid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
