# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-05-22 14:07
from __future__ import unicode_literals

import commercialoperator.components.compliances.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0097_auto_20190521_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationtype',
            name='oracle_code',
            field=models.CharField(default='ABC123 GST', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposal',
            name='fee_invoice_reference',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(upload_to=commercialoperator.components.compliances.models.update_proposal_complaince_filename),
        ),
        migrations.AlterField(
            model_name='park',
            name='oracle_code',
            field=models.CharField(default='ABC123 GST', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proposaltype',
            name='name',
            field=models.CharField(choices=[('T Class', 'T Class')], default='T Class', max_length=64, verbose_name='Application name (eg. T Class, Filming, Event, E Class)'),
        ),
    ]