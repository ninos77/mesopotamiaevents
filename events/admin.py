from django.contrib import admin

# Register your models here.

from .models import *

class EvantImageAdmin(admin.StackedInline):
    model = EventImage
   

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id','event_type','title','event_location','publishing_date')
    list_display_links = ('id','event_type')
    search_fields = ('event_type__name','title','event_location')
    list_filter = ('event_type__name','publishing_date')
    ordering = ('event_type','title','event_location','publishing_date')
    inlines = [EvantImageAdmin]

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    pass