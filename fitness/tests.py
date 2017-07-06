# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from fitness.forms import ResistanceSetForm, ResistanceSchemeForm, WorkoutForm
from fitness.models import Workout


class TestViews(TestCase):
    def setUp(self):
        self.user = User(username='test', email='test@email.com', first_name='test', last_name='user')
        self.user.set_password('password')
        self.user.save()

        self.workout1 = Workout(user=self.user, notes='test 1')
        self.workout1.save()

    def test_home_invalid(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(302, response.status_code)
        # assert(response.status_code == 302)  # more verbose example of line above

    def test_home_valid(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['workouts'].first(), self.workout1)

    def test_new_workout_view_invalid(self):
        response = self.client.get(reverse('new_workout'))
        self.assertEqual(302, response.status_code)

        response = self.client.post(reverse('new_workout'), {})
        self.assertEqual(302, response.status_code)

    def test_new_workout_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('new_workout'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(WorkoutForm, response.context['form'])

        data = {
            'date': '2015-07-06',
            'notes': 'this is a note'
        }
        response = self.client.post(reverse('new_workout'), data, follow=True)
        self.assertEqual(200, response.status_code)
        new_workout = Workout.objects.filter(user=self.user).last()
        self.assertEqual(data['date'], new_workout.date.strftime('%Y-%m-%d'))

        self.assertEqual(reverse('new_resistance_scheme', kwargs={'workout_id': new_workout.id}),
                         response.request['PATH_INFO'])

