from django.contrib import admin
from .models import TicketOfficer

@admin.register(TicketOfficer)
class TicketOfficerAdmin(admin.ModelAdmin):
    list_display = ('user', 'assigned_room', 'shift_start', 'shift_end', 'is_active')
    list_filter = ('is_active', 'assigned_room')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    ordering = ('-created_at',)
    autocomplete_fields = ['user', 'assigned_room']
