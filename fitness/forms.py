from django import forms

from fitness.models import Exercise, Workout, WorkoutSet


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('title', 'body_part', 'variation', 'modality')


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('date', 'notes')


class WorkoutSetForm(forms.ModelForm):
    class Meta:
        model = WorkoutSet
        fields = ('workout', 'exercise', 'reps', 'rep_style', 'intensity', 'load', 'notes')
