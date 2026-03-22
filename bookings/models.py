from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name='appointment', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='appointment', on_delete=models.CASCADE)
    appoiment_date = models.DateField()
    appoiment_time = models.TimeField()
    note = models.TextField()
    status = models.CharField(max_length=100)

class MedicalNote(models.Model):
    appoiment_id = models.ForeignKey(Appointment, related_name='medical_note', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name='patient_note', on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateField()