# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20171011_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='prepared',
            field=models.BooleanField(),
        ),
    ]