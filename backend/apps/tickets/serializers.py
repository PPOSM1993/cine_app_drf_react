from rest_framework import serializers
from .models import Ticket
from apps.reservations.models import Reservation
from apps.schedules.models import Schedule
from apps.seats.models import Seat
from django.utils import timezone

class TicketSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    movie = serializers.StringRelatedField(source='movie.title', read_only=True)
    room = serializers.StringRelatedField(read_only=True)
    seat = serializers.StringRelatedField(read_only=True)
    schedule = serializers.PrimaryKeyRelatedField(queryset=Schedule.objects.all(), required=True)
    reservation = serializers.PrimaryKeyRelatedField(queryset=Reservation.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Ticket
        fields = [
            'id', 'ticket_code', 'qr_code', 'user', 'movie', 'room', 'seat',
            'show_date', 'show_time', 'price', 'status',
            'purchase_datetime', 'schedule', 'reservation'
        ]
        read_only_fields = ['ticket_code', 'qr_code', 'purchase_datetime', 'status', 'show_date', 'show_time', 'movie', 'room', 'seat']

    def validate(self, data):
        schedule = data.get('schedule')
        reservation = data.get('reservation')
        request = self.context.get('request')

        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError('Usuario no autenticado.')

        if not schedule:
            raise serializers.ValidationError('Debe seleccionar un horario válido.')

        # 1. Validación: No se puede comprar ticket para una función pasada
        show_datetime = timezone.make_aware(
            timezone.datetime.combine(schedule.show_date, schedule.show_time)
        )
        if show_datetime < timezone.now():
            raise serializers.ValidationError('No puedes comprar un ticket para una función pasada.')

        if not reservation:
            raise serializers.ValidationError('Debe seleccionar una reserva válida para generar un ticket.')

        if reservation.user != request.user:
            raise serializers.ValidationError('Esta reserva no pertenece al usuario autenticado.')

        if reservation.schedule != schedule:
            raise serializers.ValidationError('La reserva no coincide con el horario seleccionado.')

        seat = reservation.seat

        # 2. Validación: Asiento ocupado
        if Ticket.objects.filter(seat=seat, schedule=schedule).exclude(status='cancelled').exists():
            raise serializers.ValidationError('Este asiento ya ha sido reservado para esta función.')

        # 3. Asignaciones automáticas (solo si validación pasa)
        data['user'] = request.user
        data['movie'] = schedule.movie
        data['room'] = schedule.room
        data['seat'] = seat
        data['show_date'] = schedule.show_date
        data['show_time'] = schedule.show_time
        data['price'] = schedule.price

        return data


class TicketListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    room_name = serializers.CharField(source='room.name', read_only=True)
    seat_code = serializers.CharField(source='seat.code', read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'id', 'ticket_code', 'movie_title', 'room_name', 'seat_code',
            'show_date', 'show_time', 'status'
        ]

class TicketDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    movie = serializers.StringRelatedField(read_only=True)
    room = serializers.StringRelatedField(read_only=True)
    seat = serializers.StringRelatedField(read_only=True)
    schedule = serializers.PrimaryKeyRelatedField(read_only=True)
    reservation = serializers.PrimaryKeyRelatedField(read_only=True)
    qr_code_url = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = [
            'id', 'ticket_code', 'qr_code_url', 'user', 'movie', 'room', 'seat',
            'show_date', 'show_time', 'price', 'status', 'purchase_datetime',
            'schedule', 'reservation'
        ]

    def get_qr_code_url(self, obj):
        if obj.qr_code:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.qr_code.url) if request else obj.qr_code.url
        return None
