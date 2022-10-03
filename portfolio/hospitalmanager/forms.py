from django import forms
from .models import DoctorLogin

class CreateDoctor(forms.ModelForm):
    class Meta:
        fields = ("first_name", "middle_name", "last_name", "email", "password", "specialization")
        model = DoctorLogin