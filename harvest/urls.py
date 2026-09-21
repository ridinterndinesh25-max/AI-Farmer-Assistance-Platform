from django.urls import path
from . import views


app_name = "harvest"


urlpatterns = [

    # Harvest Management
    path("",views.harvest_list, name="harvest_list"),

    # Edit Harvest
    path("edit/<int:harvest_id>/",views.edit_harvest,name="edit_harvest"),

    # Delete Harvest
    path("delete/<int:harvest_id>/",views.delete_harvest,name="delete_harvest"),

    # Complete Harvest
    path("complete/<int:harvest_id>/",views.complete_harvest,name="complete_harvest"),
    path("add/", views.add_harvest, name="add_harvest"),
]