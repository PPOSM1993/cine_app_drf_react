from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q

from .models import Room, Seat
from .serializers import RoomSerializer, SeatSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('name')
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'capacity']

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.select_related('room').all().order_by('room__name', 'row', 'number')
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['room', 'status', 'is_vip', 'is_accessible']
    search_fields = ['row']
    ordering_fields = ['room__name', 'row', 'number']

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class SeatSearchView(generics.ListAPIView):
    """
    Permite buscar asientos dentro de todas las salas.
    """
    queryset = Seat.objects.select_related('room').all()
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = self.queryset
        q = self.request.query_params.get('q')

        if q:
            queryset = queryset.filter(
                Q(row__icontains=q) |
                Q(number__icontains=q)
            )

        return queryset.order_by('room__name', 'row', 'number')
