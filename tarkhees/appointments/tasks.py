from celery import shared_task
from django.core.mail import send_mail
from twilio.rest import Client
import json

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
def send_reminder_sms(appointment_id):
    with open("config.json") as f:
        config = json.load(f)

    appointment = Appointment.objects.get(pk=appointment_id)

    client = Client(config['TWILIO_ACCOUNT_SID'], config['TWILIO_AUTH_TOKEN'])
    message = client.messages.create(
        body='You have an appointment coming up.',
        from_=config['TWILIO_PHONE_NUMBER'],
        to=appointment.phone_number
    )


@shared_task
def send_reminder_email_task(appointment_id):
    send_reminder_email(appointment_id)


@shared_task
def send_reminder_sms_task(appointment_id):
    send_reminder_sms(appointment_id)
