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
    modality = models.CharField(max_length=50, help_text='Method of exercise',
                                choices=MODALITY_CHOICES)

    def __str__(self):
        return self.title


class Workout(models.Model):
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '{} on {}'.format(self.user.username, datetime.strftime(self.date, '%m-%d-%Y'))



class ResistanceScheme(models.Model):
    workout = models.ForeignKey(Workout)
    exercise = models.ForeignKey(Exercise)
    variation = models.CharField(max_length=100, blank=True, null=True)
    rep_style = models.CharField(max_length=20, choices=REP_STYLE_CHOICES)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} | {}'.format(self.workout, self.exercise)



class ResistanceSet(models.Model):
    scheme = models.ForeignKey(ResistanceScheme)
    reps = models.IntegerField()
    intensity = models.FloatField()
    load = models.IntegerField(help_text='Weight in pounds')

    @property
    def work(self):
        if self.reps <= 12:
            return int((self.reps * self.load * .033) + self.load)
        else:
            return ''

    def set_rep_style(self):
        if self.reps > 0 and self.reps <= 5:
            return 'Strength/Power'
        if self.reps > 5 and self.reps <= 12:
            return 'Hypertrophy'
        if self.reps > 12:
            return 'Endurance'

    def __str__(self):
        return '{} - {} @ {}'.format(self.scheme, self.reps, self.load)


class CardioScheme(models.Model):
    workout = models.ForeignKey(Workout)
    exercise = models.ForeignKey(Exercise)
    variation = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return ''


class CardioDistance(models.Model):
    scheme = models.ForeignKey(CardioScheme)
    start = models.TimeField(null=True, blank=True)
    stop = models.TimeField(null=True, blank=True)
    distance = models.FloatField()
    measurement = models.CharField(max_length=200)
    # TODO - add choices for measurement field


class CardioInterval(models.Model):
    scheme = models.ForeignKey(CardioScheme)
    action_start = models.TimeField(null=True, blank=True)
    action_stop = models.TimeField(null=True, blank=True)
    rest_start = models.TimeField(null=True, blank=True)
    rest_stop = models.TimeField(null=True, blank=True)
    # TODO create method to populate start and stop time length entry (ex. 5 min 10 sec)


class CardioRepetition(models.Model):
    scheme = models.ForeignKey(CardioScheme)
    quanity = models.IntegerField()
    start = models.TimeField(null=True, blank=True)
    stop = models.TimeField(null=True, blank=True)

























