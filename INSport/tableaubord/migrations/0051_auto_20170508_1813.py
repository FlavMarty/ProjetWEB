# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 18:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0050_auto_20170508_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 8, 18, 13, 7, 197885), verbose_name='Date/heure evenement '),
        ),
    ]
