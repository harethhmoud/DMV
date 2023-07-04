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


def edit(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/edit.html', {'form': form})


def delete(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('index')
    return render(request, 'appointments/delete.html', {'appointment': appointment})


def create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create.html', {'form': form})
