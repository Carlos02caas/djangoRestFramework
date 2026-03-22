from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
    
    def validate(self, data):
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        qualification = data.get("qualification")

        patient_exists = Doctor.objects.filter(
            first_name__iexact=first_name,
            last_name__iexact=last_name,
            qualification__iexact=qualification
        ).exists()

        if patient_exists:
            raise serializers.ValidationError(
                "Ya existe un doctor con el mismo nombre, apellido y qualificación."
            )

        return data

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'
