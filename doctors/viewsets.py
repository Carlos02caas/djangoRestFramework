from rest_framework import viewsets
from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer
from .models import Doctor, Department, DoctorAvailability

class DoctorsViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DepartmentsViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()