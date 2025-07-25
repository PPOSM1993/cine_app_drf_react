from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'type', 'status', 'is_read', 'created_at', 'sent_at', 'read_at')
    list_filter = ('type', 'status', 'created_at', 'sent_at')
    search_fields = ('title', 'message', 'user__email')
    readonly_fields = ('created_at', 'sent_at', 'read_at')

    def is_read(self, obj):
        return obj.is_read
    is_read.boolean = True
    is_read.short_description = 'Read?'
