from django.db import models

class ServiceBooking(models.Model):
    SERVICE_CHOICES = [
        ('Service 1', 'Service 1'),
        ('Service 2', 'Service 2'),
        ('Service 3', 'Service 3'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    service_date = models.DateTimeField()
    special_request = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service_type}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
