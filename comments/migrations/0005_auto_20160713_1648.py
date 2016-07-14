# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_account_valid'),
        ('comments', '0004_comment_readed'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_forward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_forward', to='accounts.Account'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_from', to='accounts.Account'),
        ),
    ]