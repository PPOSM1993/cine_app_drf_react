from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ticket
from .serializers import TicketSerializer, TicketListSerializer, TicketDetailSerializer
from .filters import TicketFilter

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().select_related('user', 'movie', 'room', 'seat')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TicketFilter
    search_fields = ['ticket_code', 'user__email', 'movie__title']
    ordering_fields = ['purchase_datetime', 'show_date', 'status']

    def get_serializer_class(self):
        if self.action == 'list':
            return TicketListSerializer
        elif self.action == 'retrieve':
            return TicketDetailSerializer
        return TicketSerializer  # create/update

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
