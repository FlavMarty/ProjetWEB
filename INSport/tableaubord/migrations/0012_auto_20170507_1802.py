# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 18:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0011_auto_20170507_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 7, 18, 2, 26, 405135), verbose_name='Date/heure evenement '),
        ),
    ]
