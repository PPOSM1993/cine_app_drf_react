# seats/utils.py
import string
from .models import Seat

def generate_seats_for_room(room, num_rows=10, seats_per_row=10, base_price=5000):
    # Si ya existen asientos, no se vuelve a generar
    if Seat.objects.filter(room=room).exists():
        return

    total_seats = 0
    max_seats = room.capacity  # Nos aseguramos de no sobrepasar la capacidad de la sala

    for row_index in range(num_rows):
        if row_index >= len(string.ascii_uppercase):
            break  # Evita exceder letras disponibles (A-Z)
        row_letter = string.ascii_uppercase[row_index]
        for seat_number in range(1, seats_per_row + 1):
            if total_seats >= max_seats:
                return
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
            total_seats += 1
