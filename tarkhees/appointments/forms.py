from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appointment
from tempus_dominus.widgets import DatePicker


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'date', 'status', 'location', 'phone_number']
        widgets = {
            'date': DatePicker(options={
                'format': 'YYYY-MM-DD HH:mm',
                'useCurrent': True,
                'collapse': False,
            }, attrs={
                'append': 'fa fa-calendar',
            }),
        }


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    national_id = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "phone_number", "national_id")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user






