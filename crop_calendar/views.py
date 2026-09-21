from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import CropCalendar


@login_required
def crop_calendar(request):

    activities = CropCalendar.objects.filter(
        farmer=request.user
    ).order_by("activity_date")

    return render(
        request,
        "crop_calendar/calendar.html",
        {
            "activities": activities
        }
    )


@login_required
def add_activity(request):

    if request.method == "POST":

        crop_name = request.POST.get("crop_name")
        activity = request.POST.get("activity")
        activity_title = request.POST.get("activity_title")
        description = request.POST.get("description")
        activity_date = request.POST.get("activity_date")

        CropCalendar.objects.create(
            farmer=request.user,
            crop_name=crop_name,
            activity=activity,
            activity_title=activity_title,
            description=description,
            activity_date=activity_date
        )

        return redirect("crop_calendar")

    return render(
        request,
        "crop_calendar/add_activity.html"
    )


@login_required
def complete_activity(request, activity_id):

    activity = CropCalendar.objects.get(
        id=activity_id,
        farmer=request.user
    )

    activity.completed = True
    activity.save()

    return redirect("crop_calendar")