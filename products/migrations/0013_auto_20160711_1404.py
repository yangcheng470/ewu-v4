# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('sale', '在售'), ('sold', '已售')], default='sale', max_length=4),
        ),
    ]