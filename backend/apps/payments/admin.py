from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'amount',
        'method',
        'status',
        'ticket',
        'reservation',
        'transaction_code',
        'paid_at',
    )
    list_filter = ('status', 'method', 'paid_at')
    search_fields = ('user__email', 'ticket__ticket_code', 'transaction_code')
    readonly_fields = ('paid_at', 'created_at', 'updated_at')
    ordering = ('-paid_at',)

    fieldsets = (
        (None, {
            'fields': ('user', 'amount', 'method', 'status')
        }),
        ('Relacionados', {
            'fields': ('ticket', 'reservation')
        }),
        ('Transacción', {
            'fields': ('transaction_code',)
        }),
        ('Tiempos', {
            'fields': ('paid_at', 'created_at', 'updated_at')
        }),
    )
