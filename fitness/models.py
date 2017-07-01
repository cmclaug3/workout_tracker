# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


REP_STYLE_CHOICES = (
    ('str', 'Strength'),
    ('hypertrophy', 'Hypertrophy'),
    ('power', 'Power'),
    ('endurance', 'Endurance'),
)


BODY_PART_CHOICES = (
    ('arms', 'Arms'),
    ('legs', 'Legs'),
    ('chest', 'Chest'),
    ('back', 'Back'),
    ('shoulder', 'Shoulder'),
    ('core', 'Core'),
)


MODALITY_CHOICES = (
    ('barbell', 'Barbell'),
    ('kettlebell', 'Kettlebell'),
    ('dumbbell', 'Dumbbell'),
    ('machine', 'Machine'),
    ('cable', 'Cable'),
    ('smith', 'Smith'),
    ('band', 'Band'),
    ('body-weight', 'Body Weight'),
)


class Exercise(models.Model):
    title = models.CharField(max_length=200)
    body_part = models.CharField(max_length=50, choices=BODY_PART_CHOICES)
    variation = models.CharField(max_length=100, blank=True, null=True)
    modality = models.CharField(max_length=50, help_text='Method of exercise',
                                choices=MODALITY_CHOICES)

    def __str__(self):
        if self.variation:
            return '{} {}'.format(self.title, self.variation)
        return self.title


class Workout(models.Model):
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} on {}'.format(self.user.username,
                                 datetime.strftime(self.date, '%Y-%m-%d'))


class WorkoutSet(models.Model):
    workout = models.ForeignKey(Workout)
    exercise = models.ForeignKey(Exercise)
    reps = models.IntegerField()
    rep_style = models.CharField(max_length=20, choices=REP_STYLE_CHOICES)
    notes = models.TextField(null=True, blank=True)
    intensity = models.IntegerField()
    load = models.IntegerField(help_text='Weight in pounds')

    @property
    def work(self):
        return (self.load * self.reps * 0.033) + self.load
