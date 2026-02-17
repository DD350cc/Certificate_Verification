from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Certificate
from .serializers import CertificateSerializer


@api_view(['GET'])
def verify_certificate(request):
    number = request.GET.get('number','').strip()
    if not number:
        return Response({"exists": False, "message":"Certificate number is required"}, status=400)

    cert = Certificate.objects.filter(certificate_num__iexact=number).first()
    
    if not cert:
        return Response({"exists":False, "message" : "Certificate does not exist"})
    
    return Response({
            "exists":True,
            "data": {
                "candidate_name" : cert.candidate_name,
                "course_name" : cert.course_name,
                "issuer" : cert.issuer,
                "certificate_url" : cert.certificate_url,
                "issued_date" : cert.issued_date.strftime("%Y-%m-%d")
            }
        })
    


class CertificateAdminViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]