from django.db import models
from django.contrib.auth.models import User


class DiseaseDetection(models.Model):

    farmer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="disease_detections"
    )

    crop_name = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to="disease_images/"
    )

    disease_name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    confidence = models.FloatField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.crop_name} - {self.disease_name or 'Pending'}"