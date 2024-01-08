from django.db import models
from django.contrib.auth.models import AbstractUser


class TeacherModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)

class StudentModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)

class AppointmentModel(models.Model):
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField() #('email address'), blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    from_datetime = models.DateTimeField(null=True, blank=True)
    to_datetime = models.DateTimeField(null=True, blank=True)


