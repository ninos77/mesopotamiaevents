from django.db import models
from django_countries.fields import CountryField
from mesopotamiaevents import settings
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
# Create your models here.



def get_event_image_path(self,filname):
  return f'event_images/{self.post_by_id}/{filname}'


def get_event_images_path(self,filname):
  return f'event_images/{self.event.post_by_id}/{filname}'




class EventType(models.Model):
  name = models.CharField(max_length=100)


  def __str__(self):
    return self.name


class Event(models.Model):

  title = models.CharField(max_length=250)
  #event_type = models.CharField(max_length=30,choices=event_choices,blank=False,default=None)
  event_location = CountryField(blank_label='Country',blank=False,default=None)
  event_description = RichTextField(blank =True)
  publishing_date = models.DateTimeField(auto_now_add=True)
  post_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user')
  event_type= models.ForeignKey('EventType',on_delete=models.CASCADE,default=None,related_name='event')
  video_link = models.URLField(_("Your Video Link"),max_length=255,unique=True,blank=True)
  image = models.ImageField(_("Your Main Image"),upload_to=get_event_image_path,blank=True,null=True)
  slug = models.SlugField(default='slug')
  hit = models.PositiveIntegerField(default=0)


  def __str__(self):
    return self.title

  def save(self,*args,**kwargs):
    self.slug = slugify(self.title)
    super(Event, self).save(*args,**kwargs)


  class Meta:
    ordering = ('-id',)


class EventImage(models.Model):
  event = models.ForeignKey(Event,on_delete=models.CASCADE)
  image = models.ImageField(upload_to=get_event_images_path,blank=True,null=True)

  def __str__(self):
    return self.event.title