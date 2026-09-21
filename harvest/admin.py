from django.contrib import admin
from .models import Harvest


@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = (
        'crop_name',
        'expected_harvest_date',
        'actual_harvest_date',
        'quantity',
        'quantity_unit',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'quantity_unit',
    )

    search_fields = (
        'crop_name',
        'notes',
    )

    ordering = (
        '-created_at',
    )