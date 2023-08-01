from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import index, today, register_employee, detail

app_name = 'appointments'

urlpatterns = [
    path("", views.index, name='index'),
    path('<int:appointment_id>/detail/', views.detail, name='detail'),
    path('today/', today, name='today-appointments'),
    path('create/', views.create, name='create'),
    path('edit/<int:appointment_id>/', views.edit, name='edit'),
    path('delete/<int:appointment_id>/', views.delete, name='delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logged_out/', LoginView.as_view(template_name='logged_out.html'), name='logged_out'),
    path('registration/register_employee/', register_employee, name='register-employee'),
]
