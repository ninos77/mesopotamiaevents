from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):

  modele = Account

  list_display = ('email','first_name','last_name','date_joined','is_active','is_staff')
  list_display_links = ('email', 'first_name')
  list_editable = ('is_active','is_staff')
  search_fields = ('email','first_name', 'last_name')
  list_filter = ('email','first_name', 'last_name')
  ordering = ('email','first_name')
  readonly_fields = ['date_joined']

  add_fieldsets = (
    (None,{
      'classes':('wide',),
      'fields': ('email','first_name','last_name','password1','password2','is_active'),
    }),
  )

  fieldsets = (
      (None, {"fields": ('email','first_name','last_name','password')}),
      ('Permission', {"fields": ('is_active','is_staff')}),

  )
  



admin.site.register(Account,AccountAdmin)
