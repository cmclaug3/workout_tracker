# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from fitness.models import Exercise, Workout, WorkoutSet


admin.site.register(Exercise)


class WorkoutSetInline(admin.StackedInline):
    model = WorkoutSet


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    inlines = (WorkoutSetInline, )
