from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from .viewsets import PatientsViewSet, InsuranceViewSet, MedicalRecordViewSet

#from .views import list_patients,detail_patient
from .views import ListPatientsview, DetailPatientView, ListInsuranceview, DetailInsuranceView, ListMedicalRecordview, DetailMedicalRecordView

router = DefaultRouter()
router.register(r'patients', PatientsViewSet)
router.register(r'insurance', InsuranceViewSet)
router.register(r'medicalRecord', MedicalRecordViewSet)
urlpatterns = router.urls

"""
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
"""