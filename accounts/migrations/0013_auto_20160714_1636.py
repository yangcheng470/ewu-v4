# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20160714_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='sex',
            field=models.CharField(choices=[('M', '男'), ('F', '女'), ('U', '未知')], default='U', max_length=1),
        ),
    ]
