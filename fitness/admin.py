# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from fitness.models import Exercise, Workout, ResistanceScheme, ResistanceSet
from fitness.models import CardioScheme, CardioDistance, CardioInterval, CardioRepetition

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(ResistanceScheme)
admin.site.register(ResistanceSet)
admin.site.register(CardioScheme)
admin.site.register(CardioDistance)
admin.site.register(CardioInterval)
admin.site.register(CardioRepetition)












# admin.site.register(Exercise)


# class WorkoutSetInline(admin.StackedInline):
#     model = WorkoutSet


# @admin.register(Workout)
# class WorkoutAdmin(admin.ModelAdmin):
#     inlines = (WorkoutSetInline, )
