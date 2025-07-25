from django.db import models
from django.contrib.auth import get_user_model
from apps.seats.models import Room  # si tienes Room en seats

User = get_user_model()

class TicketOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ticket_officer_profile')
    assigned_room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name='ticket_officers')
    shift_start = models.TimeField(null=True, blank=True)
    shift_end = models.TimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ticket Officer"
        verbose_name_plural = "Ticket Officers"

    def __str__(self):
        return f"{self.user.get_full_name()} - Room: {self.assigned_room}"
