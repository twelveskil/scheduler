#pylint: disable=E1101
from django.urls import path
from . import views

urlpatterns = [
    path("", views.calendar_index, name="calendar_index"),
    path("event_create", views.event_create, name="event_create")
]
