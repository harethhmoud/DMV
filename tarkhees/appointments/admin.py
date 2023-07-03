from django.contrib import admin
from .models import Appointment, Location
from .forms import AppointmentForm


class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentForm


# Register your models here.
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Location)
