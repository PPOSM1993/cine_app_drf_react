from django.db import models
from django.conf import settings
from apps.seats.models import *
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

    def __str__(self):
        return self.name


class Format(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ej: 2D, 3D, IMAX

    class Meta:
        verbose_name = 'Formato'
        verbose_name_plural = 'Formatos'

    def __str__(self):
        return self.name

class Subtitle(models.Model):
    language = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Subtítulo'
        verbose_name_plural = 'Subtítulos'

    def __str__(self):
        return self.language


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        return self.name


class Movie(models.Model):
    CLASSIFICATION_CHOICES = [
        ('TE', 'Todo espectador'),
        ('7+', 'Mayores de 7 años'),
        ('14+', 'Mayores de 14 años'),
        ('18+', 'Mayores de 18 años'),
    ]

    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    duration_minutes = models.PositiveIntegerField()
    classification = models.CharField(max_length=10, choices=CLASSIFICATION_CHOICES)
    subtitles = models.ManyToManyField(Subtitle, related_name='movies', blank=True)
    countries = models.ManyToManyField(Country, related_name='movies')

    poster = models.ImageField(upload_to='movies/posters/', blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True)
    director = models.CharField(max_length=200, blank=True, null=True)
    main_cast = models.TextField(blank=True, null=True, help_text='Lista separada por comas o JSON con actores.')
    production_company = models.CharField(max_length=200, blank=True, null=True)
    original_language = models.CharField(max_length=100, blank=True, null=True)
    expected_audience = models.PositiveIntegerField(blank=True, null=True, help_text='Número estimado de asistentes.')
    is_scheduled = models.BooleanField(default=True, help_text='Marca si será exhibida próximamente.')
    release_date = models.DateField()
    pre_sale_date = models.DateField(blank=True, null=True)
    end_showing_date = models.DateField(blank=True, null=True)


    genres = models.ManyToManyField(Genre, related_name='movies')
    formats = models.ManyToManyField(Format, related_name='movies')

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'
        ordering = ['-release_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()  # Por ejemplo, de 1 a 5 estrellas
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'user')

class MovieImage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='movies/gallery/')
    caption = models.CharField(max_length=255, blank=True, null=True)


class Award(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    won = models.BooleanField(default=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='awards')


class Like(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked = models.BooleanField(default=True)  # Puede ser útil si luego se permite dislike
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'user')

class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="showtimes")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    format = models.ForeignKey(Format, on_delete=models.SET_NULL, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.movie.title} - {self.start_time} ({self.room.name})"
