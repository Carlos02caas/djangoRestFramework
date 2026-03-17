from django.contrib import admin
from django.urls import path
from .views import ListDoctorsView, DetailDoctorView


urlpatterns = [
    path('doctors/', ListDoctorsView.as_view()),
    path('doctors/<int:pk>/', DetailDoctorView.as_view()),
]