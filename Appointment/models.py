from django.db import models
#from django.contrib.auth.models import AbstractUser
#from django.contrib.auth  import get_user_model
#from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class AppointmentModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField() #('email address'), blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
