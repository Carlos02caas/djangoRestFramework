from django.contrib import admin
from django.urls import path

#from .views import list_patients,detail_patient
from .views import ListPatientsview, DetailPatientView, ListInsuranceview, DetailInsuranceView, ListMedicalRecordview, DetailMedicalRecordView


urlpatterns = [
    #path('patients/', list_patients),
    #path('patients/<int:pk>/', detail_patient),
    path('patients/', ListPatientsview.as_view()),
    path('patients/<int:pk>/', DetailPatientView.as_view()),
    path('insurance/', ListInsuranceview.as_view()),
    path('insurance/<int:pk>/', DetailInsuranceView.as_view()),
    path('medicalRecord/', ListMedicalRecordview.as_view()),
    path('medicalRecord/<int:pk>/', DetailMedicalRecordView.as_view()),
]