from rest_framework import serializers
from apps.schedules.models import Schedule
from apps.movies.models import Movie
from django.utils import timezone
from datetime import datetime, timedelta


class ScheduleSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()
    room_name = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = '__all__'

    def get_movie_title(self, obj):
        return obj.movie.title if obj.movie else None

    def get_room_name(self, obj):
        return obj.room.name if obj.room else None

    def validate(self, data):
        movie = data.get('movie')
        room = data.get('room')
        day = data.get('day')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time >= end_time:
            raise serializers.ValidationError("La hora de inicio debe ser menor que la de término.")

        if movie and not movie.is_active:
            raise serializers.ValidationError("La película debe estar activa para ser agendada.")

        if movie:
            expected_duration = timedelta(minutes=movie.duration_minutes)
            actual_duration = datetime.combine(day, end_time) - datetime.combine(day, start_time)
            if actual_duration < expected_duration:
                raise serializers.ValidationError("El tiempo disponible es menor que la duración de la película.")

        overlapping = Schedule.objects.filter(
            room=room,
            day=day
        ).exclude(id=self.instance.id if self.instance else None).filter(
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if overlapping.exists():
            raise serializers.ValidationError("Ya existe una función agendada en ese rango de tiempo para esta sala.")

        if Schedule.objects.filter(
            movie=movie, room=room, day=day, start_time=start_time
        ).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("Ya existe una función idéntica registrada.")

        return data


class ScheduleListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    room_name = serializers.CharField(source='room.name', read_only=True)
    duration = serializers.SerializerMethodField()
    start_time_local = serializers.SerializerMethodField()
    end_time_local = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    is_today = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = [
            'id', 'movie_title', 'room_name', 'day',
            'start_time_local', 'end_time_local', 'duration',
            'price', 'is_today'
        ]

    def get_duration(self, obj):
        start = datetime.combine(obj.day, obj.start_time)
        end = datetime.combine(obj.day, obj.end_time)
        return str(end - start)

    def get_start_time_local(self, obj):
        dt = datetime.combine(obj.day, obj.start_time)
        return timezone.localtime(timezone.make_aware(dt)).strftime("%H:%M")

    def get_end_time_local(self, obj):
        dt = datetime.combine(obj.day, obj.end_time)
        return timezone.localtime(timezone.make_aware(dt)).strftime("%H:%M")

    def get_is_today(self, obj):
        today = timezone.localdate()
        return obj.day == today
