
from datetime import datetime, time, timedelta, date
from django.shortcuts import render, HttpResponse
from .models import AppointmentModel
import pandas as pd

def appointment_view(request):
    context={}
    if request.method == 'POST':
        teacher = request.POST.get('teacher',None)
        student = request.POST.get('student',None)
        name = request.POST.get('name',None)  # .objects.all().first()
        email = request.POST.get('email',None)
        text = request.POST.get('text',None)
        phone = request.POST.get('phone',None)
        from_datetime = request.POST.get('from_datetime',None)
        to_datetime = request.POST.get('to_datetime',None)
        AppointmentModel.objects.create(
            teacher=teacher,
            student=student,
            name=name,
            email=email,
            text=text,
            phone=phone,
            from_datetime=from_datetime,
            to_datetime=to_datetime
        )
        conflict=AppointmentModel.objects.all()
        ls=conflict.values('from_datetime','to_datetime')
        freedatelist = pd.date_range(
            start=min(x.get('from_datetime') for x in ls if datetime.date(x.get('from_datetime')) == datetime.date(datetime.fromisoformat(from_datetime).astimezone(tz=None))),
            end=max(x.get('to_datetime') for x in ls if datetime.date(x.get('to_datetime')) == datetime.date(datetime.fromisoformat(to_datetime).astimezone(tz=None))),
            freq='120min').tolist()
        for i in freedatelist:
            for j in range(0, len(conflict)):
                if ls[j].get('from_datetime').astimezone(tz=None) <= i <= ls[j].get('to_datetime').astimezone(tz=None):
                    if i in freedatelist:
                        freedatelist.remove(i)
        for i in range (0,len(conflict)):
            if (ls[i].get('from_datetime').astimezone(tz=None)>=datetime.fromisoformat(from_datetime).astimezone(tz=None)<=ls[i].get('to_datetime').astimezone(tz=None)
                    or ls[i].get('from_datetime').astimezone(tz=None)>=datetime.fromisoformat(to_datetime).astimezone(tz=None)<=ls[i].get('to_datetime').astimezone(tz=None)):
                print(ls[i].get('from_datetime'))
                return HttpResponse("this meeting conflicts with other meetings")
            elif time(10)>=datetime.fromisoformat(from_datetime).time() or datetime.fromisoformat(from_datetime).time()>=time(18):
                return HttpResponse("it's not working hours choose different time")
            elif (timedelta(minutes=10)<ls[i].get('to_datetime').astimezone(tz=None)-ls[i].get('from_datetime').astimezone(tz=None)
                  or ls[i].get('to_datetime').astimezone(tz=None)-ls[i].get('from_datetime').astimezone(tz=None)>timedelta(hours=2)):
                return HttpResponse("This meeting's duration is inappropirate pliz choose between 30 and 120 minutes time period")
            else:
                return HttpResponse("Thanks for the Appointment")
    else:
        return render(request, 'appointment.html', context)

    return render(request,'appointment.html',context)

