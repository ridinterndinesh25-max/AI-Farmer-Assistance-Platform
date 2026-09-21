from django.db import models


class MarketPrice(models.Model):
    crop = models.CharField(max_length=100)
    mandi = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, default="per quintal")
    change = models.CharField(max_length=20, default="0%")
    status = models.CharField(max_length=10, default="up")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.crop} - ₹{self.price}"