# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171010_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='item_name',
        ),
    ]
