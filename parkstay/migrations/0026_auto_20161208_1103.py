# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-08 03:03
from __future__ import unicode_literals
import os
from django.db import migrations
from django.core.management import call_command

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))

def load_fixture(apps, schema_editor):
    call_command('loaddata', os.path.join(fixture_dir, 'closure_reasons.json'))
    call_command('loaddata', os.path.join(fixture_dir, 'open_reasons.json'))
    call_command('loaddata', os.path.join(fixture_dir, 'price_reasons.json'))
    call_command('loaddata', os.path.join(fixture_dir, 'max_stay_reasons.json'))

class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0025_auto_20161208_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='closurereason',
            old_name='deletable',
            new_name='editable',
        ),
        migrations.RenameField(
            model_name='maximumstayreason',
            old_name='deletable',
            new_name='editable',
        ),
        migrations.RenameField(
            model_name='pricereason',
            old_name='deletable',
            new_name='editable',
        ),
        migrations.RunPython(load_fixture)
    ]
