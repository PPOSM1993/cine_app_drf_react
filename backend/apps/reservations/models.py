# backend/apps/reservations/models.py

from django.conf import settings
from django.db import models
from apps.schedules.models import Schedule
from apps.seats.models import Seat

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('paid', 'Pagada'),
        ('cancelled', 'Cancelada'),
        ('expired', 'Expirada'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='reservations')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Reserva #{self.id} - {self.user} - {self.schedule}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'


class ReservationSeat(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='reserved_seats')
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)  # Redundante, pero ayuda a validar
    is_reserved = models.BooleanField(default=True)

    def __str__(self):
        return f'Asiento {self.seat} reservado en {self.schedule}'

    class Meta:
        unique_together = ('seat', 'schedule')
        verbose_name = 'Asiento reservado'
        verbose_name_plural = 'Asientos reservados'
