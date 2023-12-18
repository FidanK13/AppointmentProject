from django.db import models
#from django.contrib.auth.models import AbstractUser
#from django.contrib.auth  import get_user_model
#from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class AppointmentModel(models.Model):
    r=models.DateTimeField