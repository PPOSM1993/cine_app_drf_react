from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'ticket_code', 'user', 'movie', 'room', 'seat',
        'show_date', 'show_time', 'status', 'purchase_datetime'
    )
    list_filter = ('status', 'show_date', 'movie', 'room')
    search_fields = ('ticket_code', 'user__username', 'movie__title')
    readonly_fields = ('ticket_code', 'qr_code', 'purchase_datetime')
    date_hierarchy = 'show_date'
    ordering = ('-purchase_datetime',)

    fieldsets = (
        (None, {
            'fields': (
                'ticket_code', 'qr_code', 'user', 'movie', 'room', 'seat',
                'show_date', 'show_time', 'price', 'status',
                'purchase_datetime', 'schedule', 'reservation'
            )
        }),
    )
