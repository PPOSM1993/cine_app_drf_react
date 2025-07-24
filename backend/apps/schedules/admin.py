# apps/schedules/admin.py
from django.contrib import admin
from apps.schedules.models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'room', 'start_time', 'end_time')
    list_filter = ('room', 'movie', 'start_time')
    search_fields = ('movie__title', 'room__name')
    ordering = ('-start_time',)
