from django.db import models
from django.contrib.auth import get_user_model
from apps.movies.models import Movie
from apps.authentication.models import User

User = get_user_model()

class Promotion(models.Model):
    PERCENTAGE = 'percentage'
    FIXED = 'fixed'

    DISCOUNT_TYPE_CHOICES = [
        (PERCENTAGE, 'Percentage'),
        (FIXED, 'Fixed amount'),
    ]

    DAYS_OF_WEEK = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]


    code = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=6, decimal_places=2)  # 20.00%, or $2000

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    is_active = models.BooleanField(default=True)
    usage_limit = models.PositiveIntegerField(null=True, blank=True)  # null = unlimited
    used_count = models.PositiveIntegerField(default=0)

    applicable_movies = models.ManyToManyField(Movie, blank=True, related_name="promotions")
    min_purchase_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    auto_apply = models.BooleanField(default=False)
    valid_weekdays = models.JSONField(blank=True, null=True)  # e.g. [2, 5] for Wed and Sat
    max_discount_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    #applicable_customer_types = models.ManyToManyField(CustomerType, blank=True)


    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_promotions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date', '-created_at']

    def __str__(self):
        return f"{self.code} - {self.title}"

    def is_valid(self):
        from django.utils import timezone
        now = timezone.now()
        if not self.is_active:
            return False
        if self.start_date > now or self.end_date < now:
            return False
        if self.usage_limit and self.used_count >= self.usage_limit:
            return False
        return True
