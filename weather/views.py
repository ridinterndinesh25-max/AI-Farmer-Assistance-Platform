import requests

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def weather_home(request):

    weather_data = None
    error = None

    if request.method == "POST" or request.GET.get("refresh") == "1":

        city = request.POST.get("city", "").strip()

        if city:

            url = "https://api.openweathermap.org/data/2.5/weather"

            params = {
                "q": city,
                "appid": settings.OPENWEATHER_API_KEY,
                "units": "metric",
            }

            try:

                response = requests.get(
                    url,
                    params=params,
                    timeout=10
                )

                data = response.json()

                if response.status_code == 200:

                    weather_data = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temperature": round(data["main"]["temp"], 1),
                        "feels_like": round(data["main"]["feels_like"], 1),
                        "humidity": data["main"]["humidity"],
                        "pressure": data["main"]["pressure"],
                        "wind_speed": data["wind"]["speed"],
                        "description": data["weather"][0]["description"],
                        "icon": data["weather"][0]["icon"],
                        "rainfall": data.get("rain", {}).get("1h", 0),
                        "description": data["weather"][0]["description"],
                        "main": data["weather"][0]["main"],
                        "is_day": data["weather"][0]["icon"].endswith("d"),
                    }

                else:

                    error = data.get(
                        "message",
                        "Weather data nahi mila."
                    )

            except requests.RequestException:

                error = "Weather service se connection nahi ho pa raha."

        else:

            error = "Please city name enter karo."

    return render(
        request,
        "weather/weather.html",
        {
            "weather": weather_data,
            "error": error,
        }
    )
