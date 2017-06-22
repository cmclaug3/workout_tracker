# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

from fitness.models import Workout

def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse('account_login'))

    context = {
        'workouts': Workout.objects.filter(user=request.user),
    }
    return render(request, 'home.html', context)


def single_workout(request, workout_id):
    if not request.user.is_authenticated:
        return redirect(reverse('account_login'))

    # TODO: handle case where no workout with id found or invalid user
    workout = Workout.objects.get(user=request.user, pk=workout_id)
    context = {
        'workout': workout,
    }
    return render(request, 'fitness/single.html', context)
