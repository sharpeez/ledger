# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-27 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0015_auto_20170830_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oracleinterface',
            name='receipt_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
