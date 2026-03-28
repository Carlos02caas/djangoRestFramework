from rest_framework import viewsets, decorators, response, permissions
from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer
from .models import Doctor, Department, DoctorAvailability
from .permissions import IsDoctor
from bookings.serializers import ApointmentSerializer
from bookings.models import Appointment

class DoctorsViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsDoctor]

    @decorators.action(['POST'], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        
        doctor.save()
        return response.Response({
            'status': 'El doctor esta de vacaciones',
            'doctor': doctor.id
        })

    @decorators.action(['POST'], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        
        doctor.save()
        return response.Response({
            'status': 'El doctor no esta de vacaciones',
            'doctor': doctor.id
        })
    
    @decorators.action(['POST','GET'], detail=True, serializer_class=ApointmentSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()
        

        if request.method == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = ApointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response({
                'status': 'Se ha creado un nuevo cita',
                'appointment': serializer.data
            }) 
        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = ApointmentSerializer(appointments, many=True)
            return response.Response({
                'appointments': serializer.data
            })

class DepartmentsViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

