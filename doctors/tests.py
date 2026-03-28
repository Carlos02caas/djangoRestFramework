from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from patients.models import Patient
from doctors.models import Doctor


# Create your tests here.
class DoctorViewSetTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Carlos',
            last_name='Perez',
            date_of_birth='1990-01-01',
            contact_number='123456789',
            email='carlos@example.com',
            address='Calle de la casa, 123',
            medical_history='No tengo historial de medicamentos'
        )
        self.doctor = Doctor.objects.create(
            first_name='Juan',
            last_name='Moralez',
            qualification='Medico',
            contact_number='123456789',
            email='jusn@example.com',
            address='Calle de la casa, 123',
            biography='Soy un doctor',
            is_on_vacation=False
        )
        self.client = APIClient()

    def test_list_should_rturn_200(self):
        url = reverse('doctor-appointments', kwargs={'pk': self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    