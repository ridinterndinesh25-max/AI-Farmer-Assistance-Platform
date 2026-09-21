from django.urls import path
from . import views

urlpatterns = [
    path("", views.crop_recommendation, name="crop_recommendation"),
]