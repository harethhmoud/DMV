from django.contrib import admin
from .models import Appointment, Location, Employee
from .forms import AppointmentForm


class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentForm


# Register your models here.
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Location)
admin.site.register(Employee)