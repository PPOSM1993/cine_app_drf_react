# promotions/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PromotionViewSet, PublicPromotionListView

router = DefaultRouter()
router.register(r'', PromotionViewSet, basename='promotion')

urlpatterns = [
    path('public/', PublicPromotionListView.as_view(), name='promotion-public'),
    path('', include(router.urls)),
]
