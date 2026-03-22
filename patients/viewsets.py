from rest_framework.viewsets import ModelViewSet
from .models import Patient, Insurance, MedicalRecord
from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer

class PatientsViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class InsuranceViewSet(ModelViewSet):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()

class MedicalRecordViewSet(ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()