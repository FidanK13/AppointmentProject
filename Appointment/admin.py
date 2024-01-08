from django.contrib import admin
from .models import AppointmentModel, TeacherModel, StudentModel


admin.site.register(AppointmentModel)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)
