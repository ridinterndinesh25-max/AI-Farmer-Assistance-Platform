from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CropForm
from .models import Crop


@login_required
def crop_list(request):
    crops = Crop.objects.filter(
        farmer=request.user
    ).order_by("-created_at")

    return render(
        request,
        "crops/crop_list.html",
        {"crops": crops}
    )


@login_required
def add_crop(request):
    if request.method == "POST":
        form = CropForm(request.POST)

        if form.is_valid():
            crop = form.save(commit=False)
            crop.farmer = request.user
            crop.save()

            return redirect("crop_list")
    else:
        form = CropForm()

    return render(
        request,
        "crops/add_crop.html",
        {"form": form}
    )
@login_required
def edit_crop(request, crop_id):

    crop = Crop.objects.get(
        id=crop_id,
        farmer=request.user
    )

    if request.method == "POST":
        form = CropForm(
            request.POST,
            instance=crop
        )

        if form.is_valid():
            form.save()
            return redirect("crop_list")

    else:
        form = CropForm(instance=crop)

    return render(
        request,
        "crops/edit_crop.html",
        {"form": form, "crop": crop}
    )
@login_required
def delete_crop(request, crop_id):

    crop = Crop.objects.get(
        id=crop_id,
        farmer=request.user
    )

    if request.method == "POST":
        crop.delete()
        return redirect("crop_list")

    return render(
        request,
        "crops/delete_crop.html",
        {"crop": crop}
    )