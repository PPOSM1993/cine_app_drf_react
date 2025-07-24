from django.contrib import admin
from .models import (
    Genre, Format, Subtitle, Country, Tag,
    Movie, Rating, MovieImage, Award, Like, ShowTime
)
from apps.seats.models import Room  # en caso de que se quiera usar en filtro

class MovieImageInline(admin.TabularInline):
    model = MovieImage
    extra = 1


class AwardInline(admin.TabularInline):
    model = Award
    extra = 1


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1


class LikeInline(admin.TabularInline):
    model = Like
    extra = 1


class ShowTimeInline(admin.TabularInline):
    model = ShowTime
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'classification', 'release_date', 'is_active', 'is_scheduled']
    list_filter = ['classification', 'genres', 'formats', 'is_active', 'is_scheduled']
    search_fields = ['title', 'director', 'main_cast', 'production_company']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-release_date']
    inlines = [MovieImageInline, AwardInline, RatingInline, LikeInline, ShowTimeInline]
    filter_horizontal = ['genres', 'formats', 'subtitles', 'countries']

    fieldsets = (
        ('Información General', {
            'fields': ('title', 'slug', 'synopsis', 'poster', 'trailer_url')
        }),
        ('Detalles de Producción', {
            'fields': ('director', 'main_cast', 'production_company', 'original_language')
        }),
        ('Fechas', {
            'fields': ('release_date', 'pre_sale_date', 'end_showing_date')
        }),
        ('Clasificación y Estado', {
            'fields': ('classification', 'is_active', 'is_scheduled', 'expected_audience')
        }),
        ('Relaciones', {
            'fields': ('genres', 'formats', 'subtitles', 'countries')
        }),
        ('Tiempos', {
            'fields': ('duration_minutes',)
        }),
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Subtitle)
class SubtitleAdmin(admin.ModelAdmin):
    list_display = ['language']
    search_fields = ['language']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(ShowTime)
class ShowTimeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'room', 'start_time', 'end_time', 'format', 'price', 'is_active')
    list_filter = ('room', 'format', 'start_time', 'is_active')
    search_fields = ('movie__title', 'room__name')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'score', 'created_at']
    search_fields = ['movie__title', 'user__username']
    autocomplete_fields = ['movie', 'user']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'liked', 'created_at']
    search_fields = ['movie__title', 'user__username']
    autocomplete_fields = ['movie', 'user']


@admin.register(MovieImage)
class MovieImageAdmin(admin.ModelAdmin):
    list_display = ['movie', 'caption']
    search_fields = ['movie__title', 'caption']
    autocomplete_fields = ['movie']


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['movie', 'name', 'category', 'year', 'won']
    list_filter = ['year', 'won']
    search_fields = ['movie__title', 'name', 'category']
    autocomplete_fields = ['movie']
