# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-01 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0039_approval_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='proposal_type',
            field=models.CharField(choices=[('new_licence', 'New Licence'), ('amendment', 'Amendment'), ('renewal', 'Renewal')], default='new_licence', max_length=40, verbose_name='Proposal Type'),
        ),
    ]
