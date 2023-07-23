from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import index, today, register_employee

urlpatterns = [
    path("", views.index, name='index'),
    path('<int:appointment_id>/detail/', views.detail, name='detail'),
    path('today/', today, name='today-appointments'),
    path('create/', views.create, name='create'),
    path('edit/<int:appointment_id>/', views.edit, name='edit'),
    path('delete/<int:appointment_id>/', views.delete, name='delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/register_employee/', register_employee, name='register-employee'),
]
