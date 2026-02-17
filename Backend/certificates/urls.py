from django.urls import path, include, re_path
from django.views.generic import TemplateView
from .views import CertificateAdminViewSet, verify_certificate
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('admin', CertificateAdminViewSet, basename='certificate-admin')

urlpatterns = [
    path('verify/', verify_certificate),
    path('', include(router.urls))
]

urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html")),
]
