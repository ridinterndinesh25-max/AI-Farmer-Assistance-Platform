from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from notifications.services.weather_notifications import (
    check_weather_notification
)


class Command(BaseCommand):

    help = "Check weather and create farmer notifications"

    def handle(self, *args, **options):

        users = User.objects.filter(is_active=True)

        for user in users:
            check_weather_notification(user)

        self.stdout.write(
            self.style.SUCCESS(
                "Weather notifications checked successfully."
            )
        )