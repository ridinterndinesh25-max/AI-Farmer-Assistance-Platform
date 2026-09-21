from django.contrib import admin
from .models import MarketPrice


@admin.register(MarketPrice)
class MarketPriceAdmin(admin.ModelAdmin):
    list_display = ("crop", "mandi", "price", "unit", "change", "status", "date")
    list_filter = ("status", "date")
    search_fields = ("crop", "mandi")