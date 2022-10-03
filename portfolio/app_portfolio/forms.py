from tkinter import Widget
from django import forms
from django.forms import MultiWidget
from .models import AppUser, Patients

class CreateUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ("first_name", "middle_name", "last_name", "email", "password", "img")
        model = AppUser


class UserLogin(forms.ModelForm):

    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Enter your email address...'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Enter your password...'}))
    class Meta:
        fields = ("email", "password")
        model = AppUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['password'].label = ''

class PatientRegister(forms.ModelForm):
    class Meta:
        fields = ("full_name", "age", "address", "email", "password", "prescription", "profile")
        model = Patients