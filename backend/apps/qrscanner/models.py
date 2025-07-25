from django.db import models
from django.utils import timezone
from apps.tickets.models import Ticket
from apps.boleteros.models import TicketOfficer

class QRScanLog(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='scan_log')
    scanned_by = models.ForeignKey(TicketOfficer, on_delete=models.SET_NULL, null=True)
    scanned_at = models.DateTimeField(default=timezone.now)
    was_valid = models.BooleanField(default=False)

    def __str__(self):
        return f"Scan - {self.ticket} by {self.scanned_by} at {self.scanned_at}"
