from .serializers import PatientSerializer
from .models import Patient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

# GET /api/patients/ => List all patients
# POST /api/patients/ => Create a new patient
# GET /api/patients/<int:pk>/ => Get a patient by id
# PUT /api/patients/<int:pk>/ => Update a patient by id
#delete /api/patients/<int:pk>/ => Delete a patient by id

class ListPatientsview(APIView):
    allowed_methods = ['GET', 'POST']
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

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

class DetailPatientView(APIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']

    def queryGet(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return patient

    def get(self, request, pk):
        patient = self.queryGet(request, pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def put(self, request, pk):
        patient = self.queryGet(request, pk)
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        patient = self.queryGet(request, pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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