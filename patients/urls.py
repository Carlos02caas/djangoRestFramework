from django.contrib import admin
from django.urls import path

#from .views import list_patients,detail_patient
from .views import ListPatientsview, DetailPatientView


urlpatterns = [
    #path('patients/', list_patients),
    #path('patients/<int:pk>/', detail_patient),
    path('patients/', ListPatientsview.as_view()),
    path('patients/<int:pk>/', DetailPatientView.as_view()),
]