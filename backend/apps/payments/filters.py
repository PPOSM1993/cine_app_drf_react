import django_filters
from .models import Payment

class PaymentFilter(django_filters.FilterSet):
    paid_at__gte = django_filters.DateTimeFilter(field_name='paid_at', lookup_expr='gte')
    paid_at__lte = django_filters.DateTimeFilter(field_name='paid_at', lookup_expr='lte')
    amount__gte = django_filters.NumberFilter(field_name='amount', lookup_expr='gte')
    amount__lte = django_filters.NumberFilter(field_name='amount', lookup_expr='lte')

    class Meta:
        model = Payment
        fields = [
            'method',
            'status',
            'user',
            'ticket',
            'reservation',
            'paid_at__gte',
            'paid_at__lte',
            'amount__gte',
            'amount__lte',
        ]
