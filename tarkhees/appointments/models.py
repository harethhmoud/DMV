from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    SCHEDULED = 'SC'
    CANCELLED = 'CA'
    COMPLETED = 'CO'
    STATUS_CHOICES = [
        (SCHEDULED, 'Scheduled'),
        (CANCELLED, 'Cancelled'),
        (COMPLETED, 'Completed'),
    ]
    name = models.CharField(max_length=200)
    date = models.DateTimeField('appointment date')
    time = models.DateTimeField('appointment time')
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=SCHEDULED,
    )

    def __str__(self):
        return self.name + ", " + str(self.date) + ", " + str(self.time) + ", " + self.status
