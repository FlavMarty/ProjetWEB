# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 10:49
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0062_auto_20170510_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adherence',
            name='adherent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 10, 10, 49, 45, 738315), verbose_name='Date/heure evenement '),
        ),
    ]
