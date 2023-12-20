"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('Appointment.urls')),
    #path("appointment/",appointment_view, name='appointment'),
]
'''
data-date-format="YYYY-MM-DD" 
        <div class="w-full sm:w-half formbold-px-3">
          <div class="formbold-mb-5">
            <label for="time" class="formbold-form-label"> Time </label>
            <input
              type="time"
              name="time"
              id="time"
              class="formbold-form-input"
            />
          </div>
        </div>

< div


class ="w-full sm:w-half formbold-px-3" >

< div


class ="formbold-mb-5" >

< input
type = "text"
name = "city"
id = "city"
placeholder = "Enter city"


class ="formbold-form-input"

/ >
< / div >
< / div >
< div


class ="w-full sm:w-half formbold-px-3" >

< div


class ="formbold-mb-5" >

< input
type = "text"
name = "state"
id = "state"
placeholder = "Enter state"


class ="formbold-form-input"

/ >
< / div >
< / div >
< div


class ="w-full sm:w-half formbold-px-3" >

< div


class ="formbold-mb-5" >

< input
type = "text"
name = "post-code"
id = "post-code"
placeholder = "Post Code"


class ="formbold-form-input"

/ >
< / div >
< / div >
'''