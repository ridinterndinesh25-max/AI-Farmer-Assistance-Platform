from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import IrrigationSchedule


@login_required
def irrigation_home(request):

    schedules = IrrigationSchedule.objects.filter(
        farmer=request.user
    ).order_by("irrigation_date", "irrigation_time")

    return render(
        request,
        "irrigation/irrigation.html",
        {
            "schedules": schedules
        }
    )


@login_required
def add_irrigation(request):

    if request.method == "POST":

        crop_name = request.POST.get("crop_name")
        field_name = request.POST.get("field_name")
        irrigation_date = request.POST.get("irrigation_date")
        irrigation_time = request.POST.get("irrigation_time")
        water_amount = request.POST.get("water_amount")
        water_source = request.POST.get("water_source")
        notes = request.POST.get("notes")

        IrrigationSchedule.objects.create(
            farmer=request.user,
            crop_name=crop_name,
            field_name=field_name,
            irrigation_date=irrigation_date,
            irrigation_time=irrigation_time or None,
            water_amount=water_amount or None,
            water_source=water_source,
            notes=notes
        )

        return redirect("irrigation")

    return render(
        request,
        "irrigation/add_irrigation.html"
    )


@login_required
def complete_irrigation(request, schedule_id):

    schedule = IrrigationSchedule.objects.get(
        id=schedule_id,
        farmer=request.user
    )

    schedule.completed = True
    schedule.save()

    return redirect("irrigation")