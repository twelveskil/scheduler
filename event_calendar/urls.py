#pylint: disable=E1101
from django.urls import path
from . import views

urlpatterns = [
    path("", views.calendar_index, name="calendar_index"),
    path("create", views.event_create, name="event_create"),
    path("edit/<int:pk>/", views.event_edit, name="event_edit"),
    path("delete/<int:pk>/", views.event_delete, name="event_delete")
]
