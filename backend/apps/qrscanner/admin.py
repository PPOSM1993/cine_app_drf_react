from django.contrib import admin
from .models import QRScanLog

@admin.register(QRScanLog)
class QRScanLogAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'scanned_by', 'scanned_at', 'was_valid')
    list_filter = ('was_valid', 'scanned_at')
    search_fields = ('ticket__id', 'ticket__code', 'scanned_by__email')
    readonly_fields = ('ticket', 'scanned_by', 'scanned_at', 'was_valid')
    ordering = ('-scanned_at',)

    def has_add_permission(self, request):
        return False  # Los registros se crean solo desde el escaneo

    def has_change_permission(self, request, obj=None):
        return False  # No se pueden modificar

    def has_delete_permission(self, request, obj=None):
        return True  # Opcional: puedes dejar esto en False si no se deben borrar
