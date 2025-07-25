from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SupportCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SupportTicket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Abierto'),
        ('in_progress', 'En Proceso'),
        ('closed', 'Cerrado'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
        ('urgent', 'Urgente'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_tickets')
    category = models.ForeignKey(SupportCategory, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    response = models.TextField(blank=True, help_text="Respuesta por parte del soporte")

    def __str__(self):
        return f"{self.subject} - {self.user.email}"
