from django.db import models
from apps.movies.models import Movie
from apps.seats.models import Room
from datetime import timedelta, datetime
from django.core.exceptions import ValidationError

class Schedule(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='schedules')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='schedules')

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True)  # Se calcula automáticamente

    language = models.CharField(
        max_length=20,
        choices=[
            ('Español', 'Español'),
            ('Subtitulado', 'Subtitulado'),
            ('Inglés', 'Inglés')
        ],
        default='Español'
    )

    format = models.CharField(
        max_length=10,
        choices=[
            ('2D', '2D'),
            ('3D', '3D'),
            ('IMAX', 'IMAX')
        ],
        default='2D'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'start_time']
        unique_together = ('room', 'date', 'start_time')

    def __str__(self):
        return f'{self.movie.title} - {self.date} {self.start_time} ({self.room.name})'

    def clean(self):
        # 1. Validar que la película esté activa
        if not self.movie.is_active:
            raise ValidationError("No se puede agendar una película inactiva.")

        # 2. Validar traslapes
        overlapping = Schedule.objects.filter(
            room=self.room,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(id=self.id)

        if overlapping.exists():
            raise ValidationError("Este horario se traslapa con otro ya existente en la misma sala.")



    def save(self, *args, **kwargs):
        if self.movie and self.start_time and self.date:
            start_datetime = datetime.combine(self.date, self.start_time)
            duration = timedelta(minutes=self.movie.duration)
            self.end_time = (start_datetime + duration).time()
        super().save(*args, **kwargs)
