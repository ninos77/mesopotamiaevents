from django.urls import path
from .views import *



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create-event/', CreateEventView.as_view(), name='create_event'),
    path('event-list/', EventListView.as_view(), name='event_list'),



]