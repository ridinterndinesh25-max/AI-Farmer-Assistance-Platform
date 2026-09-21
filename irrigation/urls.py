from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.irrigation_home,
        name="irrigation"
    ),

    path(
        "add/",
        views.add_irrigation,
        name="add_irrigation"
    ),

    path(
        "complete/<int:schedule_id>/",
        views.complete_irrigation,
        name="complete_irrigation"
    ),

]