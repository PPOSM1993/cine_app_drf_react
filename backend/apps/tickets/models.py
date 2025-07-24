from django.db import models
from django.utils import timezone
import uuid

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('VALID', 'Valid'),
        ('USED', 'Used'),
        ('CANCELLED', 'Cancelled'),
        ('EXPIRED', 'Expired'),
    ]

    reservation = models.ForeignKey(
        'reservations.Reservation',
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    schedule = models.ForeignKey(
        'schedules.Schedule',
        on_delete=models.PROTECT,
        related_name='tickets'
    )
    seat = models.ForeignKey(
        'seats.Seat',
        on_delete=models.PROTECT,
        related_name='tickets'
    )
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='VALID'
    )
    issued_at = models.DateTimeField(default=timezone.now)
    used_at = models.DateTimeField(null=True, blank=True)
    qr_image = models.ImageField(
        upload_to='tickets/qrcodes/', null=True, blank=True
    )

    class Meta:
        ordering = ['-issued_at']
        unique_together = ('reservation', 'seat')

    def __str__(self):
        return f'Ticket #{self.code} - {self.user.email}'

    @property
    def is_valid(self):
        return self.status == 'VALID' and self.schedule.date >= timezone.localdate()
