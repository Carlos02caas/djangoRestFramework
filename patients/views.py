from .serializers import PatientSerializer
from .models import Patient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# GET /api/patients/ => List all patients
# POST /api/patients/ => Create a new patient
# GET /api/patients/<int:pk>/ => Get a patient by id
# PUT /api/patients/<int:pk>/ => Update a patient by id
#delete /api/patients/<int:pk>/ => Delete a patient by id

class ListPatientsview(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


""" @api_view(['GET', 'POST'])
def list_patients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
        #if serializer.is_valid(raise_exception=True):
        #    serializer.save()
        #    return Response(status=status.HTTP_201_CREATED)
         """

class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']

    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    

""""
@api_view(['GET', 'PUT','DELETE'])
def detail_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""