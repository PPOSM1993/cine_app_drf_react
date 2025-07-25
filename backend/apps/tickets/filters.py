import django_filters
from .models import Ticket

class TicketFilter(django_filters.FilterSet):
    show_date__gte = django_filters.DateFilter(field_name="show_date", lookup_expr='gte')
    show_date__lte = django_filters.DateFilter(field_name="show_date", lookup_expr='lte')
    purchase_date__range = django_filters.DateFromToRangeFilter(field_name="purchase_datetime")
    movie_title = django_filters.CharFilter(field_name="movie__title", lookup_expr='icontains')
    user_email = django_filters.CharFilter(field_name="user__email", lookup_expr='icontains')

    class Meta:
        model = Ticket
        fields = [
            'ticket_code',
            'status',
            'movie',
            'room',
            'seat',
            'show_date__gte',
            'show_date__lte',
            'purchase_date__range',
            'movie_title',
            'user_email',
        ]
