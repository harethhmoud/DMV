from django.http import HttpResponse
from .models import Appointment
from django.utils import timezone
from django.shortcuts import render


# Create your views here.
# def index(request):
#   today = timezone.localdate()
#  today_appointments = Appointment.objects.filter(date__date=today).order_by('date')
# output = ", ".join([a.name for a in today_appointments])
# context = {
#   'today_appointments': today_appointments,
# }
# return render(request, "appointments/index.html", context)

def index(request):
    all_appointments = Appointment.objects.all().order_by('date')
    context = {
        'all_appointments': all_appointments,
    }
    return render(request, "appointments/index.html", context)


def today(request):
    today = timezone.localdate()
    today_appointments = Appointment.objects.filter(date__date=today).order_by('date')
    output = ", ".join([a.name for a in today_appointments])
    context = {
        'today_appointments': today_appointments,
    }
    return render(request, "appointments/index.html", context)


def detail(request, appointment_id):
    return HttpResponse("You're looking at appointment %s." % appointment_id)


def modify(request, appointment_id):
    return HttpResponse("You're modifying appointment %s." % appointment_id)


def delete(request, appointment_id):
    return HttpResponse("You're deleting appointment %s." % appointment_id)
