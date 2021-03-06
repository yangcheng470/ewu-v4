# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20160319_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('DB', '代步'), ('DQ', '电器'), ('FS', '服饰'), ('XL', '鞋履'), ('XN', '虚拟'), ('SP', '食品'), ('SM', '数码'), ('WT', '文体'), ('SK', '书刊'), ('ZS', '装饰'), ('RY', '日用'), ('QT', '其他')], default='QT', max_length=2)),
                ('price', models.PositiveIntegerField(default=0)),
                ('condition', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('status', models.CharField(default='S', max_length=1)),
                ('imgs', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
    ]
