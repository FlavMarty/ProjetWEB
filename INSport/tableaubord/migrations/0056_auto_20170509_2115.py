# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 21:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0055_auto_20170509_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 9, 21, 15, 21, 715383), verbose_name='Date/heure evenement '),
        ),
    ]