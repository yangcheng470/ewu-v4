# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20160319_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]