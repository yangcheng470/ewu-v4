# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]