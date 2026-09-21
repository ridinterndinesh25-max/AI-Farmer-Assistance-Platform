from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.crop_calendar,
        name="crop_calendar"
    ),

    path(
        "add/",
        views.add_activity,
        name="add_calendar_activity"
    ),

    path(
        "complete/<int:activity_id>/",
        views.complete_activity,
        name="complete_calendar_activity"
    ),

]