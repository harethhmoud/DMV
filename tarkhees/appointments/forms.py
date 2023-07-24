from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appointment, Employee
from tempus_dominus.widgets import DatePicker


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'date', 'status', 'location', 'phone_number', 'email']
        widgets = {
            'date': DatePicker(options={
                'format': 'YYYY-MM-DD HH:mm',
                'useCurrent': True,
                'collapse': False,
            }, attrs={
                'append': 'fa fa-calendar',
            }),
        }


class EmployeeCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    national_id = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
        "username", "first_name", "last_name", "email", "password1", "password2", "phone_number", "national_id")

    def save(self, commit=True):
        user = super(EmployeeCreateForm, self).save(commit=False)  # This saves the form data to the database.
        user.email = self.cleaned_data["email"]  # This cleans the data and saves it to the database.
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            employee = Employee(user=user, phone_number=self.cleaned_data["phone_number"],
                                national_id=self.cleaned_data["national_id"], employee_id=self.cleaned_data["username"])
            employee.save()
        return user
