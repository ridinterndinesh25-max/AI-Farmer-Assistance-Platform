from django.contrib import admin
from .models import FarmerProfile


@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone",
        "village",
        "district",
        "state",
        "land_size",
    )