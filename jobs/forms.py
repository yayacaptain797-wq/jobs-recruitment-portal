from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = [
    "full_name",
    "email",
    "phone",
    "address",
    "cover_letter",
    "resume",
]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Enter your full name"
            }),

            "email": forms.EmailInput(attrs={
                "placeholder": "Enter your email"
            }),

            "phone": forms.TextInput(attrs={
                "placeholder": "Enter your phone number"
            }),

            "address": forms.TextInput(attrs={
                "placeholder": "Enter your address"
            }),

            "cover_letter": forms.Textarea(attrs={
                "placeholder": "Write your cover letter",
                "rows": 6
            }),
        }