from django.urls import path
from .views import *
from . import  views
from django.contrib.auth import views as auth_views


urlpatterns = [

  path('register/', views.register, name='register'),
  path('login/', auth_views.LoginView.as_view(template_name ='users/user-login.html'), name='login'),

]