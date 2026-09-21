from django.db import models
from django.contrib.auth.models import User


class CropCalendar(models.Model):

    ACTIVITY_CHOICES = [
        ("sowing", "🌱 Sowing"),
        ("irrigation", "💧 Irrigation"),
        ("fertilizer", "🧪 Fertilizer"),
        ("pesticide", "💊 Pest/Disease Control"),
        ("inspection", "🔍 Crop Inspection"),
        ("harvest", "🌾 Harvest"),
        ("other", "📌 Other"),
    ]

    farmer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="crop_calendar"
    )

    crop_name = models.CharField(max_length=100)

    activity = models.CharField(
        max_length=30,
        choices=ACTIVITY_CHOICES
    )

    activity_title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True,
        null=True
    )

    activity_date = models.DateField()

    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop_name} - {self.activity_title}"