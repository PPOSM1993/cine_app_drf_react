from django.contrib import admin
from .models import Cinema, Auditorium


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'region', 'is_active')
    list_filter = ('region', 'city', 'is_active')
    search_fields = ('name', 'address', 'city', 'region')
    ordering = ('name',)


@admin.register(Auditorium)
class AuditoriumAdmin(admin.ModelAdmin):
    list_display = ('name', 'cinema', 'total_seats', 'is_3d_enabled', 'is_active')
    list_filter = ('cinema', 'is_3d_enabled', 'is_active')
    search_fields = ('name', 'cinema__name')
    ordering = ('cinema', 'name')
