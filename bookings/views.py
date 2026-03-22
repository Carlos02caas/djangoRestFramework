from django.shortcuts import render
from .serializers import ApointmentSerializer, MedicalNoteSerializer
from .models import Appointment, MedicalNote
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class ListAppointmentView(ListAPIView, CreateAPIView):
    """ 
        Obtiene la lista de citas médicas programadas
    """
    allowed_methods = ['GET', 'POST']
    serializer_class = ApointmentSerializer
    queryset = Appointment.objects.all()

class DetailAppointmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = ApointmentSerializer
    queryset = Appointment.objects.all()

# Create your views here.
class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()