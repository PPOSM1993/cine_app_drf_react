from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import Reservation
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.select_related('user', 'schedule', 'schedule__movie', 'schedule__room').all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    # Campos para filtros exactos
    filterset_fields = {
        'status': ['exact'],
        'schedule__date': ['exact', 'gte', 'lte'],
        'schedule__movie__title': ['exact', 'icontains'],
        'user__email': ['exact', 'icontains'],
        'schedule__room__name': ['exact', 'icontains'],
    }

    # Para búsqueda por términos (en frontend tipo search input)
    search_fields = ['user__email', 'schedule__movie__title', 'schedule__room__name']

    # Ordenamiento por defecto
    ordering_fields = ['created_at', 'schedule__date', 'status']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Asigna automáticamente el usuario autenticado
