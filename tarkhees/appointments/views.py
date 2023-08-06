from django.http import HttpResponse
from .models import Appointment
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import AppointmentForm, EmployeeCreateForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.core.mail import send_mail
from datetime import timedelta
from .tasks import send_reminder_email_task


def index(request):
    all_appointments = Appointment.objects.all().order_by('date')
    context = {
        'all_appointments': all_appointments,
    }
    return render(request, "appointments/index.html", context)


@login_required
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


@login_required
@permission_required('appointments.change_appointment')
def edit(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            if appointment.email:
                date_str = appointment.date.strftime('%Y-%m-%d %H:%M:%S')
                send_mail(
                    'Appointment Update',
                    'Your appointment has been updated to ' + date_str + '.',
                    None,
                    [appointment.email],
                    fail_silently=False,
                )
            return redirect('appointments:today-appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/edit.html', {'form': form})


@login_required
@permission_required('appointments.delete_appointment')
def delete(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        if appointment.email:
            send_mail('Appointment Update', 'Your appointment has been cancelled.', None, [appointment.email], fail_silently=False,)
        appointment.delete()
        return redirect('appointments:today-appointments')
    return render(request, 'appointments/delete.html', {'appointment': appointment})


@login_required
@permission_required('appointments.add_appointment')
def create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            if appointment.email:
                date_str = appointment.date.strftime('%Y-%m-%d %H:%M:%S')
                send_mail('Appointment Update', 'Your appointment has been scheduled to ' + date_str + ".",
                          "melaniegranger62@gmail.com",
                          [appointment.email], fail_silently=False)
            reminder = appointment.date - timedelta(hours=1)
            send_reminder_email_task.apply_async((appointment.id,), eta=reminder)
            return redirect('appointments:today-appointments')
        else:
            print(form.errors)
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create.html', {'form': form})


def admin_check(user):
    return user.is_superuser


@login_required
@user_passes_test(admin_check)
def register_employee(request):
    if request.method == 'POST':  # If the form is being submitted...
        form = EmployeeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments:today-appointments')
        else:
            print(form.errors)
    else:  # If the form is being accessed for the first time
        form = EmployeeCreateForm()
    return render(request, 'registration/register_employee.html', {'form': form})
