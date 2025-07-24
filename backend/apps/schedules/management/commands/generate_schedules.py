# apps/schedules/management/commands/generate_schedules.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, datetime, time

from apps.schedules.models import Schedule
from apps.movies.models import Movie
from apps.seats.models import Room

class Command(BaseCommand):
    help = 'Genera funciones automáticamente para una sala, usando películas activas.'

    def add_arguments(self, parser):
        parser.add_argument('room_id', type=int)
        parser.add_argument('--day', type=str, default=timezone.now().date().isoformat())
        parser.add_argument('--start', type=str, default="12:00")
        parser.add_argument('--end', type=str, default="23:00")
        parser.add_argument('--gap', type=int, default=15)  # minutos entre funciones

    def handle(self, *args, **kwargs):
        room_id = kwargs['room_id']
        day = datetime.strptime(kwargs['day'], "%Y-%m-%d").date()
        start_time = datetime.combine(day, datetime.strptime(kwargs['start'], "%H:%M").time())
        end_time = datetime.combine(day, datetime.strptime(kwargs['end'], "%H:%M").time())
        gap_minutes = kwargs['gap']

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Sala con ID {room_id} no existe.'))
            return

        #movies = Movie.objects.filter(is_active=True).order_by('duration')
        movies = Movie.objects.filter(is_active=True).order_by('duration_minutes')

        if not movies.exists():
            self.stdout.write(self.style.ERROR("No hay películas activas disponibles."))
            return

        self.stdout.write(f"🎬 Generando funciones en '{room.name}' para el {day} entre {kwargs['start']} y {kwargs['end']}...")

        current_time = start_time
        movie_index = 0

        created_count = 0
        while current_time < end_time:
            movie = movies[movie_index % len(movies)]
            duration = timedelta(minutes=movie.duration)
            buffer = timedelta(minutes=gap_minutes)
            scheduled_end = current_time + duration

            if scheduled_end > end_time:
                break

            # Validación de traslapes
            overlap = Schedule.objects.filter(
                room=room,
                start_time__lt=scheduled_end,
                end_time__gt=current_time
            )
            if not overlap.exists():
                Schedule.objects.create(
                    movie=movie,
                    room=room,
                    start_time=current_time,
                    end_time=scheduled_end
                )
                created_count += 1

            current_time = scheduled_end + buffer
            movie_index += 1

        self.stdout.write(self.style.SUCCESS(f"✅ {created_count} funciones creadas correctamente."))
