from django.db import models
from django.contrib.auth.models import User


class CropRecommendation(models.Model):

    farmer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    question = models.TextField()

    image = models.ImageField(
        upload_to="crop_recommendations/",
        blank=True,
        null=True
    )

    ai_response = models.TextField(
        blank=True,
        null=True
    )

    recommended_crop = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.farmer.username} - {self.recommended_crop}"