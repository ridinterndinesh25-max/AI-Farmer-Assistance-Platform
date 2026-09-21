from django.urls import path
from . import views
from .views import disease_detection

urlpatterns = [
    path("", views.disease_detection, name="disease_detection"),
    path("result/<int:detection_id>/",views.disease_result,name="disease_result"),
    path("", disease_detection, name="disease_detection"),
      path("history/",views.detection_history,name="detection_history"),
]