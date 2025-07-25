from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CinemaViewSet,
    AuditoriumViewSet,
    PublicCinemaListView,
    PublicAuditoriumListView
)

router = DefaultRouter()
router.register(r'cinemas', CinemaViewSet, basename='cinema')
router.register(r'auditoriums', AuditoriumViewSet, basename='auditorium')

urlpatterns = [
    # Privados (CRUD)
    path('', include(router.urls)),

    # Públicos
    path('public/cinemas/', PublicCinemaListView.as_view(), name='public-cinema-list'),
    path('public/cinemas/<int:cinema_id>/auditoriums/', PublicAuditoriumListView.as_view(), name='public-auditorium-list'),
]
