# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160319_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visitors',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
