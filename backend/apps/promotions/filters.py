# promotions/filters.py
import django_filters
from .models import Promotion

class PromotionFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="start_date", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="end_date", lookup_expr="lte")
    movie_id = django_filters.NumberFilter(field_name="applicable_movies__id")
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Promotion
        fields = [
            "is_active",
            "discount_type",
            "auto_apply",
            "start_date",
            "end_date",
            "movie_id",
            "title",
        ]
