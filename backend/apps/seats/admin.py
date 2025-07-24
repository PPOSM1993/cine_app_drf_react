from django.contrib import admin
from .models import Room, Seat

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'capacity', 'total_seats')

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('room', 'row', 'number', 'status', 'is_vip', 'is_accessible')
    list_filter = ('status', 'is_vip', 'is_accessible', 'room')
