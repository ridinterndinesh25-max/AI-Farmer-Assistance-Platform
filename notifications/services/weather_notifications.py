import requests

from django.conf import settings
from notifications.models import Notification


def check_weather_notification(user):

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": "Indore,IN",
                "appid": settings.OPENWEATHER_API_KEY,
                "units": "metric",
            },
            timeout=10,
        )

        if response.status_code != 200:
            print("Weather API Error:", response.status_code)
            return

        data = response.json()

        weather_main = data["weather"][0]["main"]
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        # 🌧️ Rain Alert
        if weather_main in ["Rain", "Thunderstorm"]:

            exists = Notification.objects.filter(
                user=user,
                title="🌧️ Rain Alert",
                is_read=False
            ).exists()

            if not exists:
                Notification.objects.create(
                    user=user,
                    title="🌧️ Rain Alert",
                    message=(
                        f"Aaj {weather_description} weather hai. "
                        "Kripya pesticide spraying aur irrigation ko "
                        "temporarily avoid karein."
                    ),
                    category="weather",
                    priority="high",
                )

        # 🌡️ High Temperature Alert
        if temperature >= 40:

            exists = Notification.objects.filter(
                user=user,
                title="🌡️ High Temperature Alert",
                is_read=False
            ).exists()

            if not exists:
                Notification.objects.create(
                    user=user,
                    title="🌡️ High Temperature Alert",
                    message=(
                        f"Current temperature {temperature}°C hai. "
                        "Crop ko heat stress se bachane ke liye "
                        "proper irrigation karein."
                    ),
                    category="weather",
                    priority="high",
                )

        print("Weather notification check completed.")

    except Exception as e:
        print("Weather notification error:", e)