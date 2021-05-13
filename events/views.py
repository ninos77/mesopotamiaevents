from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView
from .models import *
from .forms import EventCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from users.models import Account,Profile
from django.db.models import F
# Create your views here.


class HomeView(ListView):
  template_name = 'events/index.html'
  context_object_name = 'events'
  model = Event 


class EventListView(LoginRequiredMixin,ListView):
  template_name = 'events/events-list.html'

  def get(self,request, **kwargs):
    events = Event.objects.filter(post_by__email=request.user.email) 
    context = {'events':events}
    return render(request, self.template_name, context)


class CreateEventView(LoginRequiredMixin,CreateView):
  template_name = 'events/create-event.html'
  form_class = EventCreationForm
  success_url = reverse_lazy("event_list")

  def form_valid(self, form):
    form.instance.post_by = self.request.user
    e = form.save()
    images = self.request.FILES.getlist("more_images")
    for i in images:
      EventImage.objects.create(event=e, image=i)
    return super().form_valid(form)



class EventDetailView(LoginRequiredMixin,DetailView):
  template_name = 'events/event-detail.html'
  model = Event
  context_object_name = 'event'

  def get (self, request, *args,**kwargs):
      self.hit = Event.objects.filter(id=self.kwargs['pk']).update(hit=F('hit')+ 1)
      return super(EventDetailView,self).get(self, request, *args,**kwargs)
  

  def get_context_data(self, **kwargs):
      context = super(EventDetailView, self).get_context_data(**kwargs)
      return context
  
def updateEvent(request, pk):
  event = get_object_or_404(Event, id=pk)
  form = EventCreationForm(instance=event)
  if request.method == 'POST':
    form = EventCreationForm(request.POST, request.FILES, instance=event)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse_lazy('event_list'))

  context = {'form':form}
  return render(request,'events/update-event.html',context)


