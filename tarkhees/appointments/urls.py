from django.urls import path
from . import views
from .views import index, detail, modify, delete, today

urlpatterns = [
    path("", views.index, name='index'),
    path('<int:appointment_id>/detail/', detail, name='detail'),
    path("<int:appointment_id>/modify/", modify, name="modify"),
    path("<int:appointment_id>/delete/", delete, name="delete"),
    path('today/', today, name='today-appointments'),
    path('create/', views.create, name='create'),
]
