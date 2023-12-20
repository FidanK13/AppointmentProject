from django.db import models
from django.contrib.auth.models import AbstractUser


class AppointmentModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField() #('email address'), blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    from_datetime = models.DateTimeField(null=True, blank=True)
    to_datetime = models.DateTimeField(null=True, blank=True)

