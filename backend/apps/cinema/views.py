from rest_framework import viewsets, filters, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cinema, Auditorium
from .serializers import CinemaSerializer, AuditoriumSerializer

# 🔒 CRUD Privado para Cinema
class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'address']
    filterset_fields = ['region', 'city', 'is_active']


# 🔒 CRUD Privado para Auditorium
class AuditoriumViewSet(viewsets.ModelViewSet):
    queryset = Auditorium.objects.all()
    serializer_class = AuditoriumSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'cinema__name']
    filterset_fields = ['cinema', 'is_active']


# 🌐 Público - Listado de Cines activos
class PublicCinemaListView(generics.ListAPIView):
    queryset = Cinema.objects.filter(is_active=True)
    serializer_class = CinemaSerializer
    permission_classes = [AllowAny]


# 🌐 Público - Listado de Auditorios por Cine
class PublicAuditoriumListView(generics.ListAPIView):
    serializer_class = AuditoriumSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        cinema_id = self.kwargs.get('cinema_id')
        return Auditorium.objects.filter(cinema_id=cinema_id, is_active=True)
