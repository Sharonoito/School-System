from django import forms
from django.forms import fields, models
from .models import Course
class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"