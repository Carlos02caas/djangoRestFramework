from rest_framework.viewsets import ModelViewSet
from .models import Appointment, MedicalNote
from .serializers import ApointmentSerializer, MedicalNoteSerializer

class AppointmentsViewSet(ModelViewSet):
    serializer_class = ApointmentSerializer
    queryset = Appointment.objects.all()

class MedicalNotesViewSet(ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()