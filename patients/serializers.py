from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import ApointmentSerializer

class PatientSerializer(serializers.ModelSerializer):

    appointment = ApointmentSerializer(many=True, read_only=True)
    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'medical_history',
            'appointment',
        ]

    def validate(self, data):
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        date_of_birth = data.get("date_of_birth")

        patient_exists = Patient.objects.filter(
            first_name__iexact=first_name,
            last_name__iexact=last_name,
            date_of_birth=date_of_birth
        ).exists()

        if patient_exists:
            raise serializers.ValidationError(
                "Ya existe un paciente con el mismo nombre, apellido y fecha de nacimiento."
            )

        return data

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'