# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 00:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0045_auto_20170508_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 8, 0, 55, 54, 554526), verbose_name='Date/heure evenement '),
        ),
    ]
