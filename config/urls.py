"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
     path("accounts/", include("accounts.urls")),
      path("", include("dashboard.urls")),
       path("crops/",include("crops.urls")),
       path("disease-detection/",include("disease_detection.urls")),
       path("weather/", include("weather.urls")),
       path("crop-recommendation/", include("crop_recommendation.urls")),
       path("market/", include("market.urls")),
       path("ai-assistant/", include("ai_assistant.urls")),
       path("notifications/", include("notifications.urls")),
       path("crop-calendar/",include("crop_calendar.urls")),
       path("irrigation/",include("irrigation.urls")),
       path('harvest/', include('harvest.urls')),
]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')