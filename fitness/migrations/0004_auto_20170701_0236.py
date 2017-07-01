# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0003_auto_20170701_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardioDistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField(blank=True, null=True)),
                ('stop', models.TimeField(blank=True, null=True)),
                ('distance', models.FloatField()),
                ('measurement', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CardioInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_start', models.TimeField(blank=True, null=True)),
                ('action_stop', models.TimeField(blank=True, null=True)),
                ('rest_start', models.TimeField(blank=True, null=True)),
                ('rest_stop', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardioRepetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanity', models.IntegerField()),
                ('start', models.TimeField(blank=True, null=True)),
                ('stop', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardioScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResistanceSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField()),
                ('intensity', models.IntegerField()),
                ('load', models.IntegerField(help_text='Weight in pounds')),
            ],
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='variation',
        ),
        migrations.RemoveField(
            model_name='resistancescheme',
            name='intensity',
        ),
        migrations.RemoveField(
            model_name='resistancescheme',
            name='load',
        ),
        migrations.RemoveField(
            model_name='resistancescheme',
            name='reps',
        ),
        migrations.AddField(
            model_name='resistancescheme',
            name='variation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resistanceset',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.ResistanceScheme'),
        ),
        migrations.AddField(
            model_name='cardioscheme',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Exercise'),
        ),
        migrations.AddField(
            model_name='cardioscheme',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Workout'),
        ),
        migrations.AddField(
            model_name='cardiorepetition',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.CardioScheme'),
        ),
        migrations.AddField(
            model_name='cardiointerval',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.CardioScheme'),
        ),
        migrations.AddField(
            model_name='cardiodistance',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.CardioScheme'),
        ),
    ]
