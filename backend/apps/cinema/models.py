from django.db import models

# Create your models here.

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Auditorium(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='auditoriums')
    name = models.CharField(max_length=100)
    total_seats = models.PositiveIntegerField()
    is_3d_enabled = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.cinema.name}"
