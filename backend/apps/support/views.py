from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import SupportCategory, SupportTicket
from .serializers import (
    SupportCategorySerializer,
    SupportTicketSerializer,
    SupportTicketListSerializer,
    SupportTicketDetailSerializer,
)
from .filters import SupportTicketFilter  # si no lo tienes aún, lo hacemos enseguida

class SupportCategoryViewSet(viewsets.ModelViewSet):
    queryset = SupportCategory.objects.all()
    serializer_class = SupportCategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']


class SupportTicketViewSet(viewsets.ModelViewSet):
    queryset = SupportTicket.objects.select_related('user', 'category').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = SupportTicketFilter
    search_fields = ['subject', 'message', 'user__email', 'category__name']
    ordering_fields = ['created_at', 'updated_at', 'priority', 'status']

    def get_serializer_class(self):
        if self.action == 'list':
            return SupportTicketListSerializer
        elif self.action == 'retrieve':
            return SupportTicketDetailSerializer
        return SupportTicketSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
