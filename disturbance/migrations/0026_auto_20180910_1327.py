# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-10 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0025_auto_20180905_1654'),
    ]

    operations = [
        # migrations.AlterField(
        #     model_name='amendmentrequest',
        #     name='reason',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disturbance.AmendmentReason'),
        # ),
        migrations.AddField(
            model_name='amendmentrequest',
            name='reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,to='disturbance.AmendmentReason'),
        ),
        # migrations.AlterField(
        #     model_name='complianceamendmentrequest',
        #     name='reason',
        #     field=models.CharField(choices=[(1, 'First reason'), (2, 'second reason')], default=1, max_length=30, verbose_name='Reason'),
        # ),
        # migrations.AlterField(
        #     model_name='proposaltype',
        #     name='name',
        #     field=models.CharField(choices=[('Disturbance', 'Disturbance'), ('Apiary', 'Apiary')], default='Disturbance', max_length=24, verbose_name='Application name (eg. Disturbance, Apiary)'),
        # ),
    ]