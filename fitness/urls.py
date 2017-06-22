from django.conf.urls import url

from fitness.views import home, single_workout

urlpatterns = [
    url(r'^workout/(?P<workout_id>[0-9]+)$', single_workout, name='single_workout'),
    url(r'^$', home, name='home'),
]