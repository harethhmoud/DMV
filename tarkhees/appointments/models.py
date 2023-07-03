from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Location(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location


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
    date = models.DateTimeField('Appointment Date')
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=SCHEDULED,
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    # This sets up a many-to-one relationship, meaning each appointment can be associated with one location,
    # but each location can have multiple appointments. Second argument deletes all appointments if loc is deleted.

    def __str__(self):
        return self.name + ", " + str(self.date) + ", " + self.status + ", " + self.location
