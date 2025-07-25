from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FidelityAccountViewSet, RewardViewSet, FidelityTransactionViewSet

router = DefaultRouter()
router.register(r'fidelity-accounts', FidelityAccountViewSet, basename='fidelity-account')
router.register(r'rewards', RewardViewSet, basename='reward')
router.register(r'transactions', FidelityTransactionViewSet, basename='fidelity-transaction')

urlpatterns = [
    path('', include(router.urls)),
]