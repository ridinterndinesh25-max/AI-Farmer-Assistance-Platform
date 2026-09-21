from django import forms
from django.contrib.auth.models import User

from .models import FarmerProfile


class FarmerRegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter password"
            }
        )
    )

    phone = forms.CharField(
        max_length=15,
        required=False
    )

    village = forms.CharField(
        max_length=100,
        required=False
    )

    district = forms.CharField(
        max_length=100,
        required=False
    )

    state = forms.CharField(
        max_length=100,
        required=False
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]