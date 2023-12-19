from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect  # , HttpResponse
from .models import AppointmentModel
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
    if request.method == 'POST':
        name = request.POST.get('name',None)  # .objects.all().first()
        email = request.POST.get('email',None)
        text = request.POST.get('text',None)
        phone = request.POST.get('phone',None)
        date = request.POST.get('date',None)
        time = request.POST.get('time',None)
        AppointmentModel.objects.create(
            name=name,
            email=email,
            text=text,
            phone=phone,
            date=date,
            time=time
        )
    else:
        #messages.error(request, AppointmentModel.errors)
        return render(request, 'appointment.html', context)

    return render(request,'appointment.html',context) #HttpResponse("home_page")
