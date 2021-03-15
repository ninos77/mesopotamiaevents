from django.contrib import admin
from .models import *
# Register your models here.

class AccountAdmin(admin.ModelAdmin):


  list_display = ('email','first_name','last_name','date_joined','is_active','is_staff')
  list_display_links = ('email', 'first_name')
  list_editable = ('is_active','is_staff')
  search_fields = ('email','first_name', 'last_name')
  list_filter = ('email','first_name', 'last_name')



admin.site.register(Account,AccountAdmin)
