# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 18:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0052_auto_20170508_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 9, 18, 44, 59, 354370), verbose_name='Date/heure evenement '),
        ),
    ]
