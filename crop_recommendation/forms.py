from django import forms


class CropRecommendationForm(forms.Form):

    nitrogen = forms.FloatField(
        label="Nitrogen (N)",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter Nitrogen value",
                "step": "any",
            }
        )
    )

    phosphorus = forms.FloatField(
        label="Phosphorus (P)",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter Phosphorus value",
                "step": "any",
            }
        )
    )

    potassium = forms.FloatField(
        label="Potassium (K)",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter Potassium value",
                "step": "any",
            }
        )
    )

    ph = forms.FloatField(
        label="Soil pH",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Example: 6.5",
                "step": "any",
            }
        )
    )

    temperature = forms.FloatField(
        label="Temperature (°C)",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter temperature",
                "step": "any",
            }
        )
    )

    humidity = forms.FloatField(
        label="Humidity (%)",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter humidity",
                "step": "any",
            }
        )
    )

    rainfall = forms.FloatField(
        label="Rainfall (mm)",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter rainfall",
                "step": "any",
            }
        )
    )