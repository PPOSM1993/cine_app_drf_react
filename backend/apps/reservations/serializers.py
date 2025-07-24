# backend/apps/reservations/serializers.py

from rest_framework import serializers
from .models import Reservation, ReservationSeat
from apps.schedules.models import Schedule
from apps.seats.models import Seat
from django.utils import timezone
from django.db import transaction


class ReservationSeatSerializer(serializers.ModelSerializer):
    seat_number = serializers.CharField(source='seat.number', read_only=True)

    class Meta:
        model = ReservationSeat
        fields = ['id', 'seat', 'seat_number', 'is_reserved']
        extra_kwargs = {
            'seat': {'write_only': True},
        }


class ReservationSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    schedule_movie = serializers.CharField(source='schedule.movie.title', read_only=True)
    schedule_start = serializers.DateTimeField(source='schedule.start_time', read_only=True)
    seats = ReservationSeatSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id', 'user', 'user_email', 'schedule', 'schedule_movie', 'schedule_start',
            'status', 'is_active', 'created_at', 'expires_at', 'seats'
        ]


class ReservationCreateSerializer(serializers.ModelSerializer):
    seat_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

    class Meta:
        model = Reservation
        fields = ['schedule', 'seat_ids']

    def validate(self, data):
        user = self.context['request'].user
        schedule = data['schedule']
        seat_ids = data['seat_ids']

        if not seat_ids:
            raise serializers.ValidationError("Debe seleccionar al menos un asiento.")

        # Verificamos que los asientos existan
        seats = Seat.objects.filter(id__in=seat_ids, room=schedule.room)
        if seats.count() != len(seat_ids):
            raise serializers.ValidationError("Uno o más asientos no existen o no pertenecen a la sala.")

        # Verificamos que no estén ya reservados para esa función
        overlapping_reservations = ReservationSeat.objects.filter(
            seat_id__in=seat_ids,
            reservation__schedule=schedule,
            reservation__status='reserved'
        )

        if overlapping_reservations.exists():
            raise serializers.ValidationError("Uno o más asientos ya están reservados para esta función.")

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        seat_ids = validated_data.pop('seat_ids')
        schedule = validated_data['schedule']

        with transaction.atomic():
            reservation = Reservation.objects.create(
                user=user,
                schedule=schedule,
                status='reserved',  # o 'pending' si usarás lógica de expiración
                is_active=True
            )

            for seat_id in seat_ids:
                seat = Seat.objects.get(id=seat_id)
                ReservationSeat.objects.create(
                    reservation=reservation,
                    seat=seat,
                    is_reserved=True
                )

        return reservation

class ReservationConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id']

    def validate(self, data):
        reservation = self.instance

        if reservation.status != 'reserved':
            raise serializers.ValidationError("Solo se pueden confirmar reservas en estado 'reserved'.")

        if reservation.expires_at and timezone.now() > reservation.expires_at:
            raise serializers.ValidationError("La reserva ha expirado y no puede ser confirmada.")

        return data

    def update(self, instance, validated_data):
        instance.status = 'confirmed'
        instance.save()
        return instance


class ReservationCancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id']

    def validate(self, data):
        reservation = self.instance

        if reservation.status in ['cancelled', 'confirmed']:
            raise serializers.ValidationError("No se puede cancelar esta reserva.")

        return data

    def update(self, instance, validated_data):
        instance.status = 'cancelled'
        instance.is_active = False
        instance.save()

        # Liberamos los asientos asociados
        ReservationSeat.objects.filter(reservation=instance).update(is_reserved=False)

        return instance