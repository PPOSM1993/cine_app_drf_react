from django.core.management.base import BaseCommand
from apps.seats.models import Room, Seat
import string

class Command(BaseCommand):
    help = 'Genera asientos para una sala específica'

    def add_arguments(self, parser):
        parser.add_argument('room_id', type=int)
        parser.add_argument('--rows', type=int, default=10)
        parser.add_argument('--seats', type=int, default=10)
        parser.add_argument('--price', type=int, default=5000)

    def handle(self, *args, **kwargs):
        room_id = kwargs['room_id']
        num_rows = kwargs['rows']
        seats_per_row = kwargs['seats']
        base_price = kwargs['price']
        total_seats = num_rows * seats_per_row

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Sala con ID {room_id} no existe.'))
            return

        # ✅ Actualizamos la capacidad de la sala
        room.capacity = total_seats
        room.save()

        # Eliminar asientos anteriores
        Seat.objects.filter(room=room).delete()
        self.stdout.write(f"Generando {num_rows} filas con {seats_per_row} asientos por fila...")

        for row_index in range(num_rows):
            row_letter = string.ascii_uppercase[row_index]
            for seat_number in range(1, seats_per_row + 1):
                Seat.objects.create(
                    room=room,
                    row=row_letter,
                    number=seat_number,
                    seat_type='normal',
                    status='available',
                    x_position=seat_number * 10,
                    y_position=row_index * 10,
                    base_price=base_price
                )

        self.stdout.write(self.style.SUCCESS('¡Asientos generados correctamente!'))
