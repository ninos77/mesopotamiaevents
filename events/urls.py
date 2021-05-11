from django.urls import path
from .views import *
from . import  views



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create-event/', CreateEventView.as_view(), name='create_event'),
    path('event-list/', EventListView.as_view(), name='event_list'),
    path('event-detail/<int:pk>/<slug:slug>', EventDetailView.as_view(), name='event_detail'),
    path('event-update/<int:pk>',views.updateEvent, name='update_event'),

]