from django.urls import path, include
from .views import CertificateAdminViewSet, verify_certificate
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('admin', CertificateAdminViewSet, basename='certificate-admin')

urlpatterns = [
    path('verify/', verify_certificate),
    path('', include(router.urls))
]


