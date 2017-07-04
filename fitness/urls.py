from django.conf.urls import url

from fitness.views import home, NewWorkoutView, single_workout, ResistanceSchemeView, ResistanceSetView

urlpatterns = [
    url(r'^workout/(?P<workout_id>[0-9]+)$', single_workout, name='single_workout'),
    url(r'^new_workout$', NewWorkoutView.as_view(), name='new_workout'),
    url(r'^new_resistance_scheme/(?P<workout_id>[0-9]+)$', ResistanceSchemeView.as_view(),
        name='new_resistance_scheme'),
    url(r'^new_resistance_set/(?P<scheme_id>[0-9]+)$', ResistanceSetView.as_view(), name='new_resistance_set'),
    # url(r'^new_workout_set/(?P<workout_id>[0-9]+)$', NewWorkoutSetView.as_view(), name='new_workout_set'),
    url(r'^$', home, name='home'),
]
