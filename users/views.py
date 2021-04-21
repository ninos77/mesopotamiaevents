from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .forms import AccountRegisterForm



# Create your views here.

class UserRegisterView(SuccessMessageMixin, CreateView):
  template_name = 'users/user-register.html'
  form_class = AccountRegisterForm
  success_url = '/'
  success_message = 'Your user account has been created'

