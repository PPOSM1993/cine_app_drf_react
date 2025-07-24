# backend/apps/reservations/admin.py

from django.contrib import admin
from .models import Reservation, ReservationSeat


class ReservationSeatInline(admin.TabularInline):
    model = ReservationSeat
    extra = 0
    readonly_fields = ('seat', 'is_reserved')
    can_delete = False


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'schedule', 'status', 'is_active', 'created_at', 'expires_at'
    )
    list_filter = ('status', 'is_active', 'created_at', 'expires_at')
    search_fields = ('user__email', 'schedule__movie__title', 'schedule__room__name')
    readonly_fields = ('created_at',)
    inlines = [ReservationSeatInline]


@admin.register(ReservationSeat)
class ReservationSeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'reservation', 'seat', 'is_reserved')
    list_filter = ('is_reserved',)
    search_fields = ('reservation__user__email', 'seat__number')
