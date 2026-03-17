from rest_framework import serializers
from .models import Apointment, MedicalNote

class ApointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apointment
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'