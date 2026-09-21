from django import forms
from .models import DiseaseDetection


class DiseaseDetectionForm(forms.ModelForm):

    class Meta:
        model = DiseaseDetection

        fields = [
            "crop_name",
            "image",
        ]

        widgets = {
            "crop_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter crop name"
                }
            ),
        }