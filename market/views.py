from django.shortcuts import render
from .models import MarketPrice


def market_prices(request):

    market_data = MarketPrice.objects.all().order_by("crop")

    return render(
        request,
        "market/market_prices.html",
        {
            "market_data": market_data
        }
    )
