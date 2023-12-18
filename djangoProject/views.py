from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect  # , HttpResponse
#from .models import AppointmentModel
#from .forms import WorkCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
#from .forms import AppointmentForm



#@login_required(login_url='login_page')
def appointment_view(request):
    context={}
    '''
    settings_queryset = Settings.objects.all().first()
    navbar_queryset = NavbarModel.objects.all()
    footer_queryset = Footer.objects.all()
    context['settings_queryset']= settings_queryset
    context['navbar_queryset']= navbar_queryset
    context['footer_queryset']= footer_queryset
    '''
    return render(request,'appointment.html',context) #HttpResponse("home_page")