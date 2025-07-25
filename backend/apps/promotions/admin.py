from django.contrib import admin
from .models import Promotion

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'title', 'discount_type', 'discount_value',
        'start_date', 'end_date', 'is_active',
        'usage_limit', 'used_count', 'auto_apply',
    )
    list_filter = (
        'discount_type', 'is_active', 'auto_apply',
        'start_date', 'end_date',
    )
    search_fields = (
        'code', 'title', 'description',
    )
    ordering = ('-start_date', '-created_at')

    filter_horizontal = ('applicable_movies',)

    readonly_fields = ('created_at', 'updated_at', 'used_count')

    fieldsets = (
        ('Información General', {
            'fields': (
                'code', 'title', 'description',
                'discount_type', 'discount_value',
                'max_discount_amount', 'auto_apply'
            )
        }),
        ('Restricciones y Aplicaciones', {
            'fields': (
                'start_date', 'end_date', 'is_active',
                'usage_limit', 'used_count',
                'applicable_movies',
                'min_purchase_amount', 'valid_weekdays',
            )
        }),
        ('Metadatos', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
