from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import *
# Create your views here.


class HomeView(ListView):
  template_name = 'events/index.html'
  context_object_name = 'events'
  model = Event 

