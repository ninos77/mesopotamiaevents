from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django import forms
from django.forms import FileInput
from .models import Event,EventImage,EventType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class EventCreationForm(forms.ModelForm):

  more_images = forms.FileField(required=False,widget=forms.FileInput(attrs={
    'class':'form-control',
    'multiple': True,
  }))
  class Meta:
    model = Event

    fields = ['title','event_location','image','event_description','event_type','video_link']

    widgets = {
      'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
      
    }


