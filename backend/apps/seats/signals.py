from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Room
from .utils import generate_seats_for_room

@receiver(post_save, sender=Room)
def create_seats_after_room_created(sender, instance, created, **kwargs):
    if created:

        generate_seats_for_room(
            room=instance,
            num_rows=8,             # Puedes cambiar esto o hacerlo configurable
            seats_per_row=12,
            base_price=6000
        )
