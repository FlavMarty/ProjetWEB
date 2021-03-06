# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adherence',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('heure', models.TimeField()),
                ('nbPlaces', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=15)),
                ('prenom', models.CharField(max_length=15)),
                ('sexe', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('tel', models.CharField(max_length=12)),
                ('mail', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='evenement',
            name='createur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableaubord.Utilisateur'),
        ),
        migrations.AddField(
            model_name='evenement',
            name='sports',
            field=models.ManyToManyField(to='tableaubord.Sport'),
        ),
        migrations.AddField(
            model_name='adherence',
            name='adherent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableaubord.Utilisateur'),
        ),
        migrations.AddField(
            model_name='adherence',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableaubord.Sport'),
        ),
    ]
