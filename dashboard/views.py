from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from crops.models import Crop


@login_required
def home(request):

    total_crops = Crop.objects.filter(
        farmer=request.user
    ).count()

    context = {
        "total_crops": total_crops,
    }

    return render(
        request,
        "dashboard/home.html",
        context
    )