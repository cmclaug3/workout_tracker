# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from fitness.models import Exercise, Workout, ResistanceScheme, ResistanceSet


admin.site.register(Exercise)


class ResistanceSetInline(admin.StackedInline):
    model = ResistanceSet


@admin.register(ResistanceScheme)
class ResistanceSchemeAdmin(admin.ModelAdmin):
    inlines = (ResistanceSetInline, )


class ResistanceSchemeInline(admin.StackedInline):
    model = ResistanceScheme


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    inlines = (ResistanceSchemeInline, )
