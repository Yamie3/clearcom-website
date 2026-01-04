from django import forms
from .models import DemoRequest

class DemoRequestForm(forms.ModelForm):
    class Meta:
        model = DemoRequest
        fields = ["name", "organization", "email", "message"]
