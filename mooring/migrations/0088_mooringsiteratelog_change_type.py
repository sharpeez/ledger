# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-19 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0087_mooringsiteratelog_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='mooringsiteratelog',
            name='change_type',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'New'), (1, 'Change'), (2, 'Delete')], default=None, null=True),
        ),
    ]
