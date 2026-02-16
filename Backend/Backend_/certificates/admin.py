from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class AdminCertificate(admin.ModelAdmin):
    fields = ['certificate_num','candidate_name','course_name','issuer','certificate_url','issued_date']
    
