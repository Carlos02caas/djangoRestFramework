from django.shortcuts import render
from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer
from .models import Doctor, Department, DoctorAvailability
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# GET /api/doctors/ => List all doctors
# POST /api/doctors/ => Create a new doctor
# GET /api/doctors/<int:pk>/ => Get a doctor by id
# PUT /api/doctors/<int:pk>/ => Update a doctor by id
# DELETE /api/doctors/<int:pk>/ => Delete a doctor by id

class ListDoctorsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class ListDepartmentView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class ListDoctorAvailabilityView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()    