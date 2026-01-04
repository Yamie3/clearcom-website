# marketing/models.py
from django.db import models

class DemoRequest(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.organization} - {self.email}"
