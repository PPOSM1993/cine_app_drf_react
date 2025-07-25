from django.db import models
from django.conf import settings
from django.utils import timezone

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('in_app', 'In-App'),
        ('email', 'Email'),
        ('push', 'Push Notification'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('read', 'Read'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES, default='in_app')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    related_object_type = models.CharField(
        max_length=100, blank=True, null=True,
        help_text="Nombre del modelo relacionado (e.g., Ticket, Promotion)"
    )
    related_object_id = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    sent_at = models.DateTimeField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} → {self.user.email}"

    @property
    def is_read(self):
        return self.status == 'read'