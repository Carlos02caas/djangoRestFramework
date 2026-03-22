from django.contrib import admin
from django.urls import path
from .views import ListAppointmentView, DetailAppointmentView, ListMedicalNoteView, DetailMedicalNoteView

from rest_framework.routers import DefaultRouter
from .viewsets import AppointmentsViewSet, MedicalNotesViewSet
router = DefaultRouter()
router.register(r'appointments', AppointmentsViewSet)
router.register(r'medicalnotes', MedicalNotesViewSet)
urlpatterns = router.urls


"""
urlpatterns = [
    path('appointments/', ListAppointmentView.as_view()),
    path('appointments/<int:pk>/', DetailAppointmentView.as_view()),
    path('medicalnotes/', ListMedicalNoteView.as_view()),
    path('medicalnotes/<int:pk>/', DetailMedicalNoteView.as_view()),
]
"""