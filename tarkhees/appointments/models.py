from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


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
    phone_number = models.CharField(max_length=10, null=True)

    # This sets up a many-to-one relationship, meaning each appointment can be associated with one location,
    # but each location can have multiple appointments. Second argument deletes all appointments if loc is deleted.

    def __str__(self):
        return self.name + ", " + str(self.date) + ", " + self.status + ", " + self.location.__str__() + ", " + str(
            self.phone_number)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # OneToOneField means each employee can have one user,
    # and each user can have one employee.
    employee_id = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    national_id = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username + ", " + self.employee_id + ", " + self.phone_number + ", " + self.national_id













