from django import forms
from .models import Crop


class CropForm(forms.ModelForm):

    class Meta:
        model = Crop

        fields = [
            "crop_name",
            "season",
            "land_area",
            "soil_type",
            "sowing_date",
            "irrigation_method",
        ]

        widgets = {
            "sowing_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }