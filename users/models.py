from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from PIL import Image
# Create your models here.

class UserManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self,email,password,**extra_fields):
    if not email:
      raise ValueError('Your Email is not correct!')
    email = self.normalize_email(email)
    user = self.model(email=email,**extra_fields)
    user.set_password(password)
    user.save(using=self.db)
    return user

  def creat_user(self,email,password=None,**extra_fields):
    extra_fields.setdefault('is_superuser',False)
    return self._create_user(email,password,**extra_fields)

  def create_superuser(self, email,password,**extra_fields):
    extra_fields.setdefault('is_superuser',True)
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('super user must have is_superuser = True')

    return self._create_user(email,password,**extra_fields)



def get_image_profile_path(self,filename):
  return f'profile_image/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
  return f'images/logo/ashor.png'


class Account(AbstractBaseUser,PermissionsMixin):
  email = models.EmailField(_('Email address'), unique=True)
  first_name = models.CharField(_('First Name'),max_length=50,blank=False)
  last_name = models.CharField(_('Last Name'),max_length=50,blank=False)
  date_joined = models.DateTimeField(_('Date joined'),auto_now_add=True)
  is_active = models.BooleanField(_('Activ'), default=True)
  is_staff = models.BooleanField(_('is staff'), default=False)
  is_admin = models.BooleanField(_('is admin'), default=False)
  country = CountryField(blank_label='Country', null=True, blank=True)


  objects = UserManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []


  def __str__(self):
    return self.first_name



  class Meta:

    verbose_name = _('user')
    verbose_name_plural = _('users')



class Profile(models.Model):
  user = models.OneToOneField(Account,on_delete= models.CASCADE,related_name='profile')
  birth_day = models.DateField(default=None,blank=True,null=True)
  profile_image = models.ImageField(max_length=255,upload_to=get_image_profile_path,null=True,blank=True,default=get_default_profile_image)

  def get_profile_image_filename(self):
    return str(self.profile_image)[str(self.profile_image).index(f'profile_image/{self.pk}/'):]


  def __str__(self):
    return self.user.first_name + ' ' +self.user.last_name

  def save(self,*args,**kwargs):
    super(Profile,self).save(*args,**kwargs)
    img = Image.open(self.profile_image)
    if img.height > 200 or img.width >200:
      new_size = (200,200)
      img.thumbnail(new_size)
      img.save(self.profile_image.path)
  
   
  @property
  def email(self):
    return self.user.email
  
  @property
  def country(self):
    return self.user.country  