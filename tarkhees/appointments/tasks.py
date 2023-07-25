from celery import shared_task
from django.core.mail import send_mail

from .models import Appointment


@shared_task
def send_reminder_email(appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    send_mail(
        'Appointment reminder',
        'You have an appointment coming up.',
        'noreply@example.com',
        [appointment.email],
        fail_silently=False,
    )


@shared_task
def send_reminder_email_task(appointment_id):
    send_reminder_email(appointment_id)

