from django.contrib import admin

# Register your models here.

from .models import *

class EvantImageAdmin(admin.StackedInline):
    model = EventImage
   

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EvantImageAdmin]
    exclude = ('image',)