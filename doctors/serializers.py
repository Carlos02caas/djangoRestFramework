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
        )

        if self.instance:
            patient_exists = patient_exists.exclude(pk=self.instance.pk)

        if patient_exists.exists():
            raise serializers.ValidationError(
                "Ya existe un doctor con el mismo nombre, apellido y qualificación."
            )
        
        if "@example.com" not in data.get("email"):
            raise serializers.ValidationError(
                "El email debe contener @example.com"
            )
        
        if (len(data.get("contact_number")) < 10) and data.get("is_on_vacation"):
            raise serializers.ValidationError(
                "El número de contacto debe tener al menos 10 dígitos"
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
