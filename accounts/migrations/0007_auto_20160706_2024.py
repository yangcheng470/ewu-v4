# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20160629_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], default='U', max_length=1),
        ),
    ]