from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Patient, Insurance, MedicalRecord
from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer

class PatientsViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    @action(['POST'], detail=True, url_path='get-historical-medical-records')
    def get_historical_medical_records(self, request, pk):
        patient = self.get_object()
        medical_records = MedicalRecord.objects.filter(patient=patient)
        serializer = MedicalRecordSerializer(medical_records, many=True)
        return Response(serializer.data)

class InsuranceViewSet(ModelViewSet):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()

class MedicalRecordViewSet(ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()