from django.db import models

class Certificate(models.Model):
    certificate_num = models.CharField(max_length=100, unique=True)
    candidate_name = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    certificate_url = models.URLField()
    issued_date = models.DateField()

    class Meta:
        ordering = ['-issued_date']

    def __str__(self):
        return f"{self.certificate_num} - {self.candidate_name}"
