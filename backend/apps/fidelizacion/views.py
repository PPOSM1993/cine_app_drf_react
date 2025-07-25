# fidelity/views.py

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import FidelityAccount, Reward, FidelityTransaction
from .serializers import (
    FidelityAccountSerializer,
    RewardSerializer,
    FidelityTransactionSerializer
)

# --- FidelityAccount ViewSet ---
class FidelityAccountViewSet(viewsets.ModelViewSet):
    queryset = FidelityAccount.objects.all().select_related('user')
    serializer_class = FidelityAccountSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__email']
    ordering_fields = ['points', 'updated_at']
    ordering = ['-updated_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# --- Reward ViewSet ---
class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['points_required', 'stock', 'created_at']
    ordering = ['-created_at']


# --- FidelityTransaction ViewSet ---
class FidelityTransactionViewSet(viewsets.ModelViewSet):
    queryset = FidelityTransaction.objects.all().select_related('account', 'reward')
    serializer_class = FidelityTransactionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['account__user__email', 'reward__name']
    ordering_fields = ['points', 'created_at', 'type']
    ordering = ['-created_at']
