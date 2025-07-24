from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies'),
router.register(r'genres', GenreViewSet, basename='genres'),
router.register(r'formats', FormatViewSet, basename='formats'),
router.register(r'showtimes', ShowTimeViewSet, basename='showtime')


urlpatterns = [
    path('', include(router.urls)),
    # Endpoint especializado para búsqueda
    path('search/', MovieSearchView.as_view(), name='movie-search'),
]