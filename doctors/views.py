from django.shortcuts import render
from .serializers import DoctorSerializer
from .models import Doctor
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
    