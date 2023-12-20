
from datetime import datetime, time
from django.shortcuts import render, HttpResponse
from .models import AppointmentModel


def appointment_view(request):
    context={}
    if request.method == 'POST':
        name = request.POST.get('name',None)  # .objects.all().first()
        email = request.POST.get('email',None)
        text = request.POST.get('text',None)
        phone = request.POST.get('phone',None)
        from_datetime = request.POST.get('from_datetime',None)
        to_datetime = request.POST.get('to_datetime',None)
        AppointmentModel.objects.create(
            name=name,
            email=email,
            text=text,
            phone=phone,
            from_datetime=from_datetime,
            to_datetime=to_datetime
        )
        conflict=AppointmentModel.objects.all()
        ls=conflict.values('from_datetime','to_datetime')
        for i in range (0,len(conflict)):
            if (ls[i].get('from_datetime').astimezone(tz=None)>=datetime.fromisoformat(from_datetime).astimezone(tz=None)<=ls[i].get('to_datetime').astimezone(tz=None)
                    or ls[i].get('from_datetime').astimezone(tz=None)>=datetime.fromisoformat(to_datetime).astimezone(tz=None)<=ls[i].get('to_datetime').astimezone(tz=None)):
                print(ls[i].get('from_datetime'))
                return HttpResponse("this meeting conflicts with other meetings")
            elif time(18)>=datetime.fromisoformat(from_datetime).time()<=time(18):
                return HttpResponse("it's not working hours choose different time")
            elif time(0,10)<ls[i].get('to_datetime').astimezone(tz=None)-ls[i].get('from_datetime').astimezone(tz=None)>time(2):
                return HttpResponse("This meeting's duration is inappropirate pliz choose between 30 and 120 minutes time period")
            else:
                return HttpResponse("Thanks for the Appointment")
    else:
        return render(request, 'appointment.html', context)

    return render(request,'appointment.html',context)
