from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class AccountAdmin(UserAdmin):
  
  inlines = (ProfileInline, )
  modele = Account

  list_display = ('id','email','first_name','last_name','date_joined','is_superuser','is_active','is_staff')
  list_display_links = ('email', 'first_name')
  list_editable = ('is_active','is_staff')
  search_fields = ('id','email','first_name', 'last_name')
  list_filter = ('email','first_name', 'last_name')
  ordering = ('email','first_name')
  readonly_fields = ['date_joined']

  add_fieldsets = (
    (None,{
      'classes':('wide',),
      'fields': ('email','first_name','last_name','password1','password2','is_active','is_staff','is_admin','country'),
    }),
  )

  fieldsets = (
      (None, {"fields": ('email','first_name','last_name','password','country')}),
      ('Permission', {"fields": ('is_active','is_staff')}),

  )

  def get_inline_instances(self, request, obj=None):
    if not obj:
      return list()
    return super(AccountAdmin, self).get_inline_instances(request, obj)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  modele = Profile
  list_display = ('user','email','country','profile_image')





admin.site.register(Account,AccountAdmin)
