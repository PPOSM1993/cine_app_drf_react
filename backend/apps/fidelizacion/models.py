# fidelity/models.py

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class FidelityAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='fidelity_account')
    points = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.points} pts"


class Reward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    points_required = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.points_required} pts)"


class FidelityTransaction(models.Model):
    class Type(models.TextChoices):
        EARN = 'earn', _('Earned')
        REDEEM = 'redeem', _('Redeemed')

    account = models.ForeignKey(FidelityAccount, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=10, choices=Type.choices)
    points = models.IntegerField()
    reward = models.ForeignKey(Reward, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.account.user.email} - {self.type} - {self.points} pts"
