from django import forms
from .models import Appointment
from tempus_dominus.widgets import DatePicker


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'date', 'status', 'location']
        widgets = {
            'date': DatePicker()  # specify date-input format
        }
