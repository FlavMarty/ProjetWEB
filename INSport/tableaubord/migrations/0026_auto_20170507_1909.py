# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 19:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0025_auto_20170507_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 7, 19, 9, 56, 799766), verbose_name='Date/heure evenement '),
        ),
    ]
