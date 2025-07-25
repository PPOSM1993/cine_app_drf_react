from rest_framework import serializers
from .models import TicketOfficer
from django.utils import timezone

class TicketOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketOfficer
        fields = '__all__'

    def validate(self, data):
        shift_start = data.get('shift_start')
        shift_end = data.get('shift_end')

        # Validación de turnos
        if shift_start and shift_end:
            if shift_start >= shift_end:
                raise serializers.ValidationError("El inicio del turno debe ser antes del fin del turno.")

        # Validación de usuario único (ya existe TicketOfficer para ese User)
        if self.instance is None:
            user = data.get('user')
            if TicketOfficer.objects.filter(user=user).exists():
                raise serializers.ValidationError("Este usuario ya está registrado como boletero.")

        return data
