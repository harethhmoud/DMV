from django.http import HttpResponse
from .models import Appointment
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import AppointmentForm


def index(request):
    all_appointments = Appointment.objects.all().order_by('date')
    context = {
        'all_appointments': all_appointments,
    }
    return render(request, "appointments/index.html", context)


def today(request):
    to_day = timezone.localdate()
    today_appointments = Appointment.objects.filter(date__date=to_day).order_by('date')
    output = ", ".join([a.name for a in today_appointments])
    context = {
        'today_appointments': today_appointments,
    }
    return render(request, "appointments/today.html", context)


def detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, "appointments/detail.html", {'appointment': appointment})


def modify(request, appointment_id):
    return HttpResponse("You're modifying appointment %s." % appointment_id)


def delete(request, appointment_id):
    return HttpResponse("You're deleting appointment %s." % appointment_id)


def create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create.html', {'form': AppointmentForm})
