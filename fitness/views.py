# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.views import View

from fitness.forms import ResistanceSetForm, ResistanceSchemeForm, WorkoutForm
from fitness.models import ResistanceScheme, Workout


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
    try:
        workout = Workout.objects.get(user=request.user, id=workout_id)
    except Workout.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'No horkout with id {}.'.format(workout_id))
        return redirect(reverse('home'))
    context = {
        'workout': workout,
    }
    return render(request, 'fitness/single.html', context)


class NewWorkoutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))
        context = {
            'form': WorkoutForm,
        }
        return render(request, 'fitness/new_workout.html', context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))
        form = WorkoutForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form,
            }
            return render(request, 'fitness/new_workout.html', context)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

        if request.POST.get('resist'):
            return redirect(reverse('new_resistance_scheme', kwargs={'workout_id': obj.id}))
        elif request.POST.get('cardio'):
            # TODO: update to point to new_cardio_scheme
            return redirect(reverse('new_resistance_scheme', kwargs={'workout_id': obj.id}))
        else:
            messages.warning(request, 'Resistance is futile?')
            return redirect(reverse('home'))


class ResistanceSchemeView(View):
    def get(self, request, workout_id):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))
        try:
            workout = Workout.objects.get(user=request.user, id=workout_id)
        except Workout.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'No horkout with id {}.'.format(workout_id))
            return redirect(reverse('home'))
        context = {
            'form': ResistanceSchemeForm(initial={'workout': workout}),
        }
        return render(request, 'fitness/new_workout_scheme.html', context)

    def post(self, request, workout_id):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))
        try:
            workout = Workout.objects.get(user=request.user, id=workout_id)
        except Workout.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'No horkout with id {}.'.format(workout_id))
            return redirect(reverse('home'))
        form = ResistanceSchemeForm(request.POST, initial={'workout': workout})
        if not form.is_valid():
            context = {
                'form': form,
            }
            return render(request, 'fitness/new_workout_scheme.html', context)
        scheme = form.save()

        if request.POST.get('num_sets'):
            num_sets = request.POST.get('num_sets')
            try:
                num_sets = int(num_sets)
                return redirect('{}?num_sets={}'.format(
                    reverse('new_resistance_set', kwargs={'scheme_id': scheme.id}),
                    num_sets))
            except TypeError:
                pass

        return redirect(reverse('new_resistance_set', kwargs={'scheme_id': scheme.id}))


class ResistanceSetView(View):
    form_set = formset_factory(ResistanceSetForm, extra=2)

    def get(self, request, scheme_id):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))

        num_sets = request.GET.get('num_sets', False)
        if num_sets:
            try:
                num_sets = int(num_sets)
                self.form_set = formset_factory(ResistanceSetForm, extra=num_sets-1)
            except TypeError:
                pass

        try:
            scheme = ResistanceScheme.objects.get(workout__user=request.user, id=scheme_id)
        except ResistanceScheme.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'No ResistanceScheme with id {}.'.format(scheme_id))
            return redirect(reverse('home'))
        context = {
            # 'form_set': form_set(),
            'form_set': self.form_set(initial=[{'scheme': scheme}, ]),
        }
        return render(request, 'fitness/new_resistance_set.html', context)

    def post(self, request, scheme_id):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))
        try:
            scheme = ResistanceScheme.objects.get(workout__user=request.user, id=scheme_id)
        except ResistanceScheme.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'No ResistanceScheme with id {}.'.format(scheme_id))
            return redirect(reverse('home'))
        form_set = self.form_set(request.POST)
        # form_set = self.form_set(request.POST, initial=[{'scheme': scheme}, ])
        # form = ResistanceSetForm(request.POST, initial={'scheme': scheme})
        if not form_set.is_valid():
            context = {
                'form_set': form_set,
            }
            return render(request, 'fitness/new_resistance_set.html', context)
        for form in form_set.forms:
            workout_set = form.save()

        if request.POST.get('add_another'):
            # return self.get(request, workout_id)
            return redirect((reverse('new_resistance_set', kwargs={'scheme_id': scheme.id})))

        if request.POST.get('save_review'):
            # return self.get(request, workout_id)
            return redirect((reverse('single_workout', kwargs={'workout_id': workout_set.scheme.workout.id})))

        # add another workout set?

        return redirect(reverse('new_resistance_scheme', kwargs={'workout_id': workout_set.scheme.workout.id}))

# class NewWorkoutSetView(View):
#     def get(self, request, workout_id):
#         if not request.user.is_authenticated:
#             return redirect(reverse('account_login'))
#         try:
#             workout = Workout.objects.get(user=request.user, id=workout_id)
#         except Workout.DoesNotExist:
#             messages.add_message(request, messages.ERROR, 'No horkout with id {}.'.format(workout_id))
#             return redirect(reverse('home'))
#         context = {
#             'form': WorkoutSetForm(initial={'workout': workout}),
#         }
#         return render(request, 'fitness/new_workout_set.html', context)
#
#     def post(self, request, workout_id):
#         if not request.user.is_authenticated:
#             return redirect(reverse('account_login'))
#         try:
#             workout = Workout.objects.get(user=request.user, id=workout_id)
#         except Workout.DoesNotExist:
#             messages.add_message(request, messages.ERROR, 'No horkout with id {}.'.format(workout_id))
#             return redirect(reverse('home'))
#         form = WorkoutSetForm(request.POST, initial={'workout': workout})
#         if not form.is_valid():
#             context = {
#                 'form': form,
#             }
#             return render(request, 'fitness/new_workout_set.html', context)
#         obj = form.save()
#
#         if request.POST.get('add_another'):
#             # return self.get(request, workout_id)
#             return redirect(reverse('new_workout_set', kwargs={'workout_id': workout_id}))
#
#         # add another workout set?
#
#         return redirect((reverse('single_workout', kwargs={'workout_id': workout_id})))
