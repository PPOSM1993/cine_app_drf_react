from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Notification
from .serializers import (
    NotificationSerializer,
    NotificationListSerializer,
    NotificationDetailSerializer,
)
from .filters import NotificationFilter

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().select_related('user')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = NotificationFilter
    search_fields = ['title', 'message']
    ordering_fields = ['created_at', 'sent_at', 'read_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return NotificationListSerializer
        elif self.action == 'retrieve':
            return NotificationDetailSerializer
        return NotificationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
