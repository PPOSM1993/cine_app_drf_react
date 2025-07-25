import django_filters
from apps.qrscanner.models import QRScanLog

class QRScanLogFilter(django_filters.FilterSet):
    ticket_code = django_filters.CharFilter(field_name='ticket__code', lookup_expr='icontains')
    ticket_showtime = django_filters.DateTimeFilter(field_name='ticket__showtime')

    class Meta:
        model = QRScanLog
        fields = {
            'was_valid': ['exact'],
            'scanned_by': ['exact'],
        }
