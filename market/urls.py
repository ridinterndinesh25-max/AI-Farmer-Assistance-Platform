from django.urls import path
from . import views

urlpatterns = [
    path("", views.market_prices, name="market_prices"),
]

