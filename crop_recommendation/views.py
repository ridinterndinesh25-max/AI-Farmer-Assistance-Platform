from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import CropRecommendationForm
from .ml_models.predictor import predict_crop


@login_required
def crop_recommendation(request):

    recommendation = None

    if request.method == "POST":

        form = CropRecommendationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            nitrogen = float(request.POST.get("nitrogen"))
            phosphorus = float(request.POST.get("phosphorus"))
            potassium = float(request.POST.get("potassium"))
            ph = float(request.POST.get("ph"))
            temperature = float(request.POST.get("temperature"))
            humidity = float(request.POST.get("humidity"))
            rainfall = float(request.POST.get("rainfall"))

            recommended_crop = predict_crop(
                nitrogen,
                phosphorus,
                potassium,
                temperature,
                humidity,
                ph,
                rainfall
            )

            recommendation = recommended_crop

    else:

        form = CropRecommendationForm()

    return render(
        request,
        "crop_recommendation/recommendation.html",
        {
            "form": form,
            "recommendation": recommendation,
        }
    )