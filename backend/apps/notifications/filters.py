import django_filters
from .models import Notification

class NotificationFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()
    sent_at = django_filters.DateFromToRangeFilter()
    read_at = django_filters.DateFromToRangeFilter()
    type = django_filters.CharFilter(lookup_expr='iexact')
    status = django_filters.CharFilter(lookup_expr='iexact')
    is_read = django_filters.BooleanFilter()

    class Meta:
        model = Notification
        fields = ['type', 'status', 'is_read', 'created_at', 'sent_at', 'read_at']
