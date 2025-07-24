# backend/apps/reservations/signals.py

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Reservation, ReservationSeat


@receiver(pre_save, sender=Reservation)
def handle_expired_reservation(sender, instance, **kwargs):
    """
    Antes de guardar, si la reserva ya expiró y sigue activa, se cancela automáticamente.
    """
    if instance.status == 'pending' and instance.expires_at < timezone.now():
        instance.status = 'expired'
        instance.is_active = False


@receiver(post_save, sender=Reservation)
def release_seats_if_cancelled(sender, instance, **kwargs):
    """
    Cuando una reserva es cancelada o expirada, liberamos los asientos.
    """
    if instance.status in ['cancelled', 'expired']:
        seats = ReservationSeat.objects.filter(reservation=instance)
        for seat in seats:
            seat.is_reserved = False
            seat.save()
