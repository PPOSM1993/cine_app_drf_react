# apps/qrscanner/views.py

from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.qrscanner.models import QRScanLog
from apps.qrscanner.serializers import QRScanLogSerializer
from apps.tickets.models import Ticket
from apps.qrscanner.filters import QRScanLogFilter

class QRScanLogViewSet(viewsets.ModelViewSet):
    queryset = QRScanLog.objects.select_related('ticket', 'scanned_by').all()
    serializer_class = QRScanLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = QRScanLogFilter  # <-- filtro personalizado aquí
    search_fields = ['ticket__code', 'scanned_by__email']
    ordering_fields = ['scanned_at', 'ticket__code']
    ordering = ['-scanned_at']

class QRPublicScanAPIView(APIView):
    """
    Escaneo público de QR. No se requiere más que autenticación del boletero.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = QRScanLogSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        scan = serializer.save()
        return Response(QRScanLogSerializer(scan).data, status=status.HTTP_201_CREATED)
