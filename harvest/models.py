from django.db import models
from django.contrib.auth.models import User


class Harvest(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Ready', 'Ready for Harvest'),
        ('Completed', 'Completed'),
    ]

    farmer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='harvests'
    )

    crop_name = models.CharField(
        max_length=100
    )

    expected_harvest_date = models.DateField()

    actual_harvest_date = models.DateField(
        blank=True,
        null=True
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    quantity_unit = models.CharField(
        max_length=20,
        default='kg'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.crop_name} - {self.status}"