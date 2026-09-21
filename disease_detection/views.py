from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import DiseaseDetectionForm
from .models import DiseaseDetection
from .ml_models.predictor import predict_disease, get_treatment


@login_required
def disease_detection(request):

    if request.method == "POST":

        form = DiseaseDetectionForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            detection = form.save(commit=False)

            detection.farmer = request.user

            detection.save()

            disease_name, confidence = predict_disease(
                detection.image.path
            )

            detection.disease_name = disease_name
            detection.confidence = confidence

            detection.save()

            return redirect(
                "disease_result",
                detection_id=detection.id
            )

    else:

        form = DiseaseDetectionForm()

    return render(
        request,
        "disease_detection/detection.html",
        {
            "form": form
        }
    )



@login_required
def disease_result(request, detection_id):

    detection = DiseaseDetection.objects.get(
        id=detection_id,
        farmer=request.user
    )

    treatment = get_treatment(detection.disease_name)

    return render(
        request,
        "disease_detection/result.html",
        {
            "detection": detection,
            "treatment": treatment,
        }
    )
@login_required
def detection_history(request):

    detections = DiseaseDetection.objects.filter(
        farmer=request.user
    ).order_by("-created_at")

    return render(
        request,
        "disease_detection/history.html",
        {
            "detections": detections
        }
    )