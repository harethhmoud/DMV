import os
from celery import Celery

# Set the default Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tarkhees.settings')

app = Celery("tarkhees")

# Use Django's settings for the Celery app.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in installed apps.
app.autodiscover_tasks()
