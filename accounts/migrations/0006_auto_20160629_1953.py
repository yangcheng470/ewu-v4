# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_account_visitors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pwd',
            field=models.CharField(max_length=128),
        ),
    ]
