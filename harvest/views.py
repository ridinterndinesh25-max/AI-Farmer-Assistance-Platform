from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages

from .models import Harvest


@login_required
def harvest_list(request):
    """
    Show all harvest records of logged-in farmer.
    """

    harvests = Harvest.objects.filter(
        farmer=request.user
    ).order_by("-created_at")

    return render(
        request,
        "harvest/harvest_list.html",
        {
            "harvests": harvests
        }
    )


@login_required
def add_harvest(request):
    """
    Add new harvest record.
    """

    if request.method == "POST":

        crop_name = request.POST.get("crop_name", "").strip()
        expected_harvest_date = request.POST.get("expected_harvest_date")
        actual_harvest_date = request.POST.get("actual_harvest_date")
        quantity = request.POST.get("quantity")
        quantity_unit = request.POST.get("quantity_unit") or "kg"
        status = request.POST.get("status") or "Pending"
        notes = request.POST.get("notes", "").strip()

        # -----------------------------------------
        # Basic validation
        # -----------------------------------------

        if not crop_name:
            messages.error(request, "Please enter crop name.")
            return redirect("harvest:add_harvest")

        if not expected_harvest_date:
            messages.error(request, "Please select expected harvest date.")
            return redirect("harvest:add_harvest")

        # -----------------------------------------
        # Actual date validation
        # -----------------------------------------

        if actual_harvest_date and actual_harvest_date < expected_harvest_date:
            messages.error(
                request,
                "Actual harvest date cannot be before expected harvest date."
            )
            return redirect("harvest:add_harvest")

        # -----------------------------------------
        # Quantity validation
        # -----------------------------------------

        if quantity:
            try:
                quantity_value = float(quantity)

                if quantity_value < 0:
                    messages.error(
                        request,
                        "Quantity cannot be negative."
                    )
                    return redirect("harvest:add_harvest")

            except ValueError:
                messages.error(
                    request,
                    "Please enter a valid quantity."
                )
                return redirect("harvest:add_harvest")
        else:
            quantity = None

        # -----------------------------------------
        # Completed status validation
        # -----------------------------------------

        if status == "Completed" and not actual_harvest_date:
            messages.error(
                request,
                "Actual harvest date is required for completed harvest."
            )
            return redirect("harvest:add_harvest")

        # -----------------------------------------
        # Create harvest record
        # -----------------------------------------

        Harvest.objects.create(
            farmer=request.user,
            crop_name=crop_name,
            expected_harvest_date=expected_harvest_date,
            actual_harvest_date=actual_harvest_date or None,
            quantity=quantity,
            quantity_unit=quantity_unit,
            status=status,
            notes=notes
        )

        messages.success(
            request,
            "Harvest record added successfully!"
        )

        return redirect("harvest:harvest_list")

    return render(
        request,
        "harvest/add_harvest.html"
    )


@login_required
def edit_harvest(request, harvest_id):
    """
    Edit existing harvest record.
    """

    harvest = get_object_or_404(
        Harvest,
        id=harvest_id,
        farmer=request.user
    )

    if request.method == "POST":

        crop_name = request.POST.get("crop_name", "").strip()
        expected_harvest_date = request.POST.get("expected_harvest_date")
        actual_harvest_date = request.POST.get("actual_harvest_date")
        quantity = request.POST.get("quantity")
        quantity_unit = request.POST.get("quantity_unit") or "kg"
        status = request.POST.get("status") or "Pending"
        notes = request.POST.get("notes", "").strip()

        # -----------------------------------------
        # Basic validation
        # -----------------------------------------

        if not crop_name:
            messages.error(request, "Please enter crop name.")
            return redirect(
                "harvest:edit_harvest",
                harvest_id=harvest.id
            )

        if not expected_harvest_date:
            messages.error(
                request,
                "Please select expected harvest date."
            )
            return redirect(
                "harvest:edit_harvest",
                harvest_id=harvest.id
            )

        # -----------------------------------------
        # Date validation
        # -----------------------------------------

        if actual_harvest_date and actual_harvest_date < expected_harvest_date:
            messages.error(
                request,
                "Actual harvest date cannot be before expected harvest date."
            )
            return redirect(
                "harvest:edit_harvest",
                harvest_id=harvest.id
            )

        # -----------------------------------------
        # Quantity validation
        # -----------------------------------------

        if quantity:
            try:
                quantity_value = float(quantity)

                if quantity_value < 0:
                    messages.error(
                        request,
                        "Quantity cannot be negative."
                    )
                    return redirect(
                        "harvest:edit_harvest",
                        harvest_id=harvest.id
                    )

            except ValueError:
                messages.error(
                    request,
                    "Please enter a valid quantity."
                )
                return redirect(
                    "harvest:edit_harvest",
                    harvest_id=harvest.id
                )
        else:
            quantity = None

        # -----------------------------------------
        # Completed validation
        # -----------------------------------------

        if status == "Completed" and not actual_harvest_date:
            messages.error(
                request,
                "Actual harvest date is required for completed harvest."
            )
            return redirect(
                "harvest:edit_harvest",
                harvest_id=harvest.id
            )

        # -----------------------------------------
        # Update record
        # -----------------------------------------

        harvest.crop_name = crop_name
        harvest.expected_harvest_date = expected_harvest_date
        harvest.actual_harvest_date = actual_harvest_date or None
        harvest.quantity = quantity
        harvest.quantity_unit = quantity_unit
        harvest.status = status
        harvest.notes = notes

        harvest.save()

        messages.success(
            request,
            "Harvest record updated successfully!"
        )

        return redirect("harvest:harvest_list")

    return render(
        request,
        "harvest/edit_harvest.html",
        {
            "harvest": harvest
        }
    )


@login_required
def delete_harvest(request, harvest_id):
    """
    Delete harvest record.
    """

    harvest = get_object_or_404(
        Harvest,
        id=harvest_id,
        farmer=request.user
    )

    if request.method == "POST":

        harvest.delete()

        messages.success(
            request,
            "Harvest record deleted successfully!"
        )

    return redirect("harvest:harvest_list")


@login_required
def complete_harvest(request, harvest_id):
    """
    Mark harvest as completed.
    """

    harvest = get_object_or_404(
        Harvest,
        id=harvest_id,
        farmer=request.user
    )

    if request.method == "POST":

        harvest.status = "Completed"
        harvest.actual_harvest_date = timezone.localdate()

        harvest.save()

        messages.success(
            request,
            "Harvest marked as completed!"
        )

    return redirect("harvest:harvest_list")