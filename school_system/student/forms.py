from django import forms
from django.forms import fields, models
from .models import Student
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"