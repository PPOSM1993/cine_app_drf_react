from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, MovieSearchView

router = DefaultRouter()
router.register(r'', MovieViewSet, basename='movies')

urlpatterns = [
    path('', include(router.urls)),

    # Endpoint especializado para búsqueda
    path('search/', MovieSearchView.as_view(), name='movie-search'),
]