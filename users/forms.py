from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django import forms
from django.forms import FileInput
from .models import Account, Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class AccountRegisterForm(UserCreationForm):

  email = forms.EmailField()

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    icons = getattr(self.Meta, 'icons', dict())

    for field_name, field in self.fields.items():
        # add form-control class to all fields
        field.widget.attrs['class'] = 'form-control'
        # set icon attr on field object
        if field_name in icons:
            field.icon = icons[field_name]
  

  
  class Meta:
    model = Account
    fields = ['email','first_name','last_name']
    icons = {'email': 'ln-icon-Mail','first_name':'ln-icon-Male','last_name':'ln-icon-Male','password1':'ln-icon-Lock-2','password2':'ln-icon-Lock-2'}


class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()

  class Meta:
    model = Account
    fields = ['email','first_name','last_name','country']



class ProfileUpdateForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = ['birth_day','profile_image']

    widgets = {
      'birth_day': forms.DateInput(attrs={'type':'date'}),
      'profile_image': FileInput(attrs={'id':'selectedFile'})
    }



    