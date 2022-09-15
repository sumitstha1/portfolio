from django import forms
from .models import AppUser, Patients

class CreateUser(forms.ModelForm):
    class Meta:
        fields = ("first_name", "middle_name", "last_name", "email", "password", "img")
        model = AppUser

class UserLogin(forms.ModelForm):
    class Meta:
        fields = ("email", "password")
        model = AppUser

class PatientRegister(forms.ModelForm):
    class Meta:
        fields = ("full_name", "age", "address", "email", "password", "prescription", "profile")
        model = Patients