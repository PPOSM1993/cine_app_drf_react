from django.contrib import admin
from .models import Genre, Format, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'classification', 'duration_minutes', 'release_date', 'is_active', 'is_scheduled')
    list_filter = ('classification', 'is_active', 'is_scheduled', 'release_date')
    search_fields = ('title', 'director', 'main_cast', 'production_company')
    filter_horizontal = ('genres', 'formats')
    readonly_fields = ('created_at', 'updated_at')
