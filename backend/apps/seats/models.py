from django.db import models

class Room(models.Model):
    ROOM_TYPES = (
        ('2D', '2D'),
        ('3D', '3D'),
        ('IMAX', 'IMAX'),
        ('4DX', '4DX'),
    )

    name = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()
    type = models.CharField(max_length=10, choices=ROOM_TYPES, default='2D')

    def __str__(self):
        return f"{self.name} ({self.type})"

    @property
    def total_seats(self):
        return self.seats.count()


class Seat(models.Model):
    STATUS_CHOICES = (
        ('available', 'Disponible'),
        ('reserved', 'Reservado'),
        ('sold', 'Vendido'),
        ('maintenance', 'En mantenimiento'),
    )

    SEAT_TYPE_CHOICES = (
        ('normal', 'Normal'),
        ('vip', 'VIP'),
        ('accessible', 'Accesible'),
        ('love_seat', 'Love Seat'),
    )

    room = models.ForeignKey(Room, related_name='seats', on_delete=models.CASCADE)
    row = models.CharField(max_length=5)
    number = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    seat_type = models.CharField(max_length=20, choices=SEAT_TYPE_CHOICES, default='normal')
    is_vip = models.BooleanField(default=False)  # Conservado por compatibilidad si ya lo usas
    is_accessible = models.BooleanField(default=False)
    # Coordenadas opcionales para layout de asientos visual
    x_position = models.IntegerField(null=True, blank=True)
    y_position = models.IntegerField(null=True, blank=True)
    # Precio base opcional
    base_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('room', 'row', 'number')
        ordering = ['row', 'number']

    def __str__(self):
        tipo = dict(self.SEAT_TYPE_CHOICES).get(self.seat_type, "")
        return f"Fila {self.row} - Asiento {self.number} ({tipo})"

    @property
    def seat_label(self):
        return f"{self.row}{self.number}"

    def save(self, *args, **kwargs):
        if self.pk is None and self.room.seats.count() >= self.room.capacity:
            raise ValueError("La sala ya alcanzó su capacidad máxima de asientos.")
        super().save(*args, **kwargs)
