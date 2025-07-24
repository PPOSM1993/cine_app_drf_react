from django.contrib import admin
from .models import Room, Seat

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'capacity', 'total_seats')
    search_fields = ('name',)  # 🔍 permite buscar por nombre
    list_filter = ('type',)    # 📂 filtrar por tipo de sala (2D, 3D, etc.)

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('room', 'row', 'number', 'status', 'is_vip', 'is_accessible')
    list_filter = ('status', 'is_vip', 'is_accessible', 'room')
    search_fields = ('row', 'number')
    ordering = ('room', 'row', 'number')

