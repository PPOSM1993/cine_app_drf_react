import django_filters
from .models import SupportTicket

class SupportTicketFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()
    status = django_filters.CharFilter(lookup_expr='iexact')
    priority = django_filters.CharFilter(lookup_expr='iexact')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    user_email = django_filters.CharFilter(field_name='user__email', lookup_expr='icontains')

    class Meta:
        model = SupportTicket
        fields = ['status', 'priority', 'category', 'created_at', 'user_email']
