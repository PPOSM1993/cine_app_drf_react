from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from utils.pagination import StandardResultsSetPagination
from django.db.models import Q
from utils.pagination import StandardResultsSetPagination

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all().order_by('name')
    serializer_class = FormatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class MovieViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para películas.
    """
    #queryset = Movie.objects.all().order_by('-release_date')
    queryset = Movie.objects.prefetch_related('genres', 'formats').order_by('-release_date')

    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    #filterset_fields = ['classification', 'is_active', 'is_scheduled', 'release_date']
    filterset_fields = ['classification', 'is_active', 'is_scheduled', 'release_date', 'genres', 'formats']

    search_fields = ['title', 'director', 'main_cast', 'production_company', 'original_language']
    ordering_fields = ['release_date', 'title', 'expected_audience']


class MovieSearchView(generics.ListAPIView):
    """
    Vista especializada para búsqueda libre.
    """
    #queryset = Movie.objects.filter(is_active=True)
    queryset = Movie.objects.prefetch_related('genres', 'formats').filter(is_active=True)

    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination  # opcional si quieres paginar resultados de búsqueda también

    def get_queryset(self):
        """
        Permite búsqueda por título, director, reparto, productora.
        """
        queryset = self.queryset
        q = self.request.query_params.get('q', '').strip()
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(director__icontains=q) |
                Q(main_cast__icontains=q) |
                Q(production_company__icontains=q)
            )

        return queryset.order_by('-release_date')


class ShowTimeViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para funciones de películas (showtimes).
    Soporta búsqueda por título de película y nombre del formato.
    """
    queryset = ShowTime.objects.select_related('movie', 'format', 'hall', 'cinema').all().order_by('-start_time')
    serializer_class = ShowTimeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['movie', 'format', 'cinema', 'hall', 'start_time']
    search_fields = ['movie__title', 'format__name', 'hall__name', 'cinema__name']
    ordering_fields = ['start_time', 'movie__title']

    def get_queryset(self):
        queryset = super().get_queryset()
        movie_title = self.request.query_params.get('movie_title')
        format_name = self.request.query_params.get('format_name')

        if movie_title:
            queryset = queryset.filter(movie__title__icontains=movie_title)
        if format_name:
            queryset = queryset.filter(format__name__icontains=format_name)

        return queryset
