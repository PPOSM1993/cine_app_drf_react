from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import TicketOfficer
from .serializers import TicketOfficerSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

class TicketOfficerViewSet(viewsets.ModelViewSet):
    queryset = TicketOfficer.objects.all().select_related('user', 'assigned_room')
    serializer_class = TicketOfficerSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible para usuarios logueados (admin o staff)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'assigned_room']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    ordering_fields = ['shift_start', 'shift_end', 'created_at']

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def public_list(self, request):
        """
        Vista pública opcional para ver boleteros activos y visibles
        """
        queryset = TicketOfficer.objects.filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
