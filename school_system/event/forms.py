from django import forms
from django.forms import fields, models
from .models import Event

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"


