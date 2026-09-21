from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):

    CATEGORY_CHOICES = [
        ("weather", "Weather"),
        ("disease", "Disease Detection"),
        ("treatment", "Treatment"),
        ("market", "Market Price"),
        ("mandi", "Best Mandi"),
        ("crop", "Crop Recommendation"),
        ("farming", "Farming Tips"),
        ("reminder", "Farm Reminder"),
        ("system", "System"),
    ]

    PRIORITY_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("normal", "Normal"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(max_length=200)

    message = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="system"
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="normal"
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"