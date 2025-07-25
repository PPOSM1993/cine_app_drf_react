# apps/qrscanner/serializers.py

from rest_framework import serializers
from django.utils import timezone
from apps.qrscanner.models import QRScanLog
from apps.tickets.models import Ticket

class QRScanLogSerializer(serializers.ModelSerializer):
    ticket_code = serializers.CharField(write_only=True)
    scanned_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    scanned_at = serializers.DateTimeField(read_only=True)
    was_valid = serializers.BooleanField(read_only=True)

    class Meta:
        model = QRScanLog
        fields = ['id', 'ticket_code', 'ticket', 'scanned_by', 'scanned_at', 'was_valid']
        read_only_fields = ['ticket']

    def validate_ticket_code(self, code):
        try:
            ticket = Ticket.objects.get(code=code)
        except Ticket.DoesNotExist:
            raise serializers.ValidationError("Ticket no encontrado.")

        if QRScanLog.objects.filter(ticket=ticket, was_valid=True).exists():
            raise serializers.ValidationError("Este ticket ya ha sido utilizado.")

        if ticket.status != 'valid':
            raise serializers.ValidationError("El ticket no es válido actualmente.")

        if ticket.showtime.end_time < timezone.now():
            raise serializers.ValidationError("Este ticket ya ha expirado.")

        return code

    def create(self, validated_data):
        code = validated_data.pop('ticket_code')
        ticket = Ticket.objects.get(code=code)
        validated_data['ticket'] = ticket
        validated_data['was_valid'] = True  # Ya fue validado en `validate_ticket_code`

        return super().create(validated_data)
