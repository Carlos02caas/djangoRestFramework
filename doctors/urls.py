from django.contrib import admin
from django.urls import path
from .views import ListDoctorsView, DetailDoctorView, ListDepartmentView, DetailDepartmentView, ListDoctorAvailabilityView, DetailDoctorAvailabilityView
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorsViewSet, DepartmentsViewSet, DoctorAvailabilityViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorsViewSet)
router.register(r'departments', DepartmentsViewSet)
router.register(r'doctorAvailability', DoctorAvailabilityViewSet)
urlpatterns = router.urls
"""

urlpatterns = [
    #path('doctors/', ListDoctorsView.as_view()),
    #path('doctors/<int:pk>/', DetailDoctorView.as_view()),
    path('departments/', ListDepartmentView.as_view()),
    path('departments/<int:pk>/', DetailDepartmentView.as_view()),
    path('doctorAvailability/', ListDoctorAvailabilityView.as_view()),
    path('doctorAvailability/<int:pk>/', DetailDoctorAvailabilityView.as_view()),
] + router.urls
"""