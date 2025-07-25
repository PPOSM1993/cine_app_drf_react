from django.db import models
from django.contrib.auth import get_user_model
from apps.tickets.models import Ticket
from apps.reservations.models import Reservation

User = get_user_model()

class PaymentMethod(models.TextChoices):
    CREDIT = 'credit', 'Crédito'
    DEBIT = 'debit', 'Débito'
    CASH = 'cash', 'Efectivo'
    GIFT_CARD = 'gift_card', 'Gift Card'
    ONLINE = 'online', 'Pago Online'  # Stripe, Transbank...

class PaymentStatus(models.TextChoices):
    PENDING = 'pending', 'Pendiente'
    COMPLETED = 'completed', 'Completado'
    FAILED = 'failed', 'Fallido'
    REFUNDED = 'refunded', 'Reembolsado'

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)

    transaction_code = models.CharField(max_length=100, blank=True, null=True)  # para integración futura
    paid_at = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pago #{self.id} - {self.user.email} - ${self.amount} - {self.get_status_display()}"
