from django.contrib.auth.models import User
from django.db import models


class Crop(models.Model):

    SEASON_CHOICES = [
        ("Kharif", "Kharif"),
        ("Rabi", "Rabi"),
        ("Zaid", "Zaid"),
        ("Other", "Other"),
    ]

    farmer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="crops"
    )

    crop_name = models.CharField(max_length=100)

    season = models.CharField(
        max_length=20,
        choices=SEASON_CHOICES
    )

    land_area = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    soil_type = models.CharField(
        max_length=100
    )

    sowing_date = models.DateField(
        null=True,
        blank=True
    )

    irrigation_method = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.crop_name} - {self.farmer.username}"