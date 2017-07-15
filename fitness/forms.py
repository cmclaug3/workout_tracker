from django import forms

from fitness.models import (Exercise, Workout, ResistanceScheme, ResistanceSet,
                            CardioScheme, CardioDistance, CardioInterval, CardioRepetition)


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('title', 'body_part', 'modality')


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('date', 'notes')


class ResistanceSchemeForm(forms.ModelForm):
    class Meta:
        model = ResistanceScheme
        fields = (
            'workout', 'exercise', 'variation', 'rep_style',
            'notes'
        )


class ResistanceSetForm(forms.ModelForm):
    class Meta:
        model = ResistanceSet
        fields = (
            'scheme', 'reps', 'intensity', 'load'
        )


class CardioSchemeForm(forms.ModelForm):
    class Meta:
        model = CardioScheme
        fields = (
            'workout', 'exercise', 'notes'
        )


class CardioDistanceForm(forms.ModelForm):
    class Meta:
        model = CardioDistance
        fields = (
            'scheme', 'start', 'stop', 'distance', 'measurement'
        )


class CardioIntervalForm(forms.ModelForm):
    class Meta:
        model = CardioInterval
        fields = (
            'scheme', 'action_start', 'action_stop', 'rest_start',
            'rest_stop'
        )


class CardioRepetitionForm(forms.ModelForm):
    class Meta:
        model = CardioRepetition
        fields = (
            'scheme', 'quantity', 'start', 'stop',
        )
