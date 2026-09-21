import requests
from django.core.management.base import BaseCommand
from market.models import MarketPrice


class Command(BaseCommand):
    help = "Update MP market prices from Mandi API"

    def handle(self, *args, **kwargs):

        url = "https://mandi-api.onrender.com/v1/prices"

        crops = [
            "Onion",
            "Wheat",
            "Soybean",
            "Maize",
            "Potato",
            "Tomato",
        ]

        total_updated = 0

        for crop in crops:

            params = {
                "state": "Madhya Pradesh",
                "commodity": crop,
            }

            try:
                response = requests.get(
                    url,
                    params=params,
                    timeout=30
                )

                if response.status_code != 200:
                    self.stdout.write(
                        self.style.WARNING(
                            f"{crop}: API Error {response.status_code}"
                        )
                    )
                    continue

                data = response.json().get("data", [])

                for item in data:

                    MarketPrice.objects.update_or_create(
                        crop=item["commodity"],
                        mandi=item["market"],
                        defaults={
                            "price": item["modal_price"],
                            "unit": "per quintal",
                            "change": "Updated",
                            "status": "up",
                        }
                    )

                total_updated += len(data)

                self.stdout.write(
                    self.style.SUCCESS(
                        f"{crop}: {len(data)} records updated"
                    )
                )

            except requests.RequestException as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"{crop}: {e}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Total market records updated: {total_updated}"
            )
        )