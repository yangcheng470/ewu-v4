# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20160712_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='phone',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='qq',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
