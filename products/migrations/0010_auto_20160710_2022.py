# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20160710_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='big_imgs',
            field=models.ImageField(default='big/default', upload_to='big'),
        ),
        migrations.AlterField(
            model_name='product',
            name='small_imgs',
            field=models.ImageField(default='small/default', upload_to='small'),
        ),
    ]
