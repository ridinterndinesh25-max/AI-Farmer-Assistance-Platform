from django.db import models
from django.contrib.auth.models import User


class IrrigationSchedule(models.Model):

    WATER_SOURCE_CHOICES = [
        ("borewell", "💧 Borewell"),
        ("canal", "🌊 Canal"),
        ("river", "🏞️ River"),
        ("rainwater", "🌧️ Rainwater"),
        ("tank", "🛢️ Water Tank"),
        ("other", "📌 Other"),
    ]

    farmer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="irrigation_schedules"
    )

    crop_name = models.CharField(
        max_length=100
    )

    field_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    irrigation_date = models.DateField()

    irrigation_time = models.TimeField(
        blank=True,
        null=True
    )

    water_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )

    water_source = models.CharField(
        max_length=30,
        choices=WATER_SOURCE_CHOICES,
        default="borewell"
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.crop_name} - {self.irrigation_date}"