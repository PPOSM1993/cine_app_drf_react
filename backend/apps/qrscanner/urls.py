# apps/qrscanner/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.qrscanner.views import QRScanLogViewSet, QRPublicScanAPIView

router = DefaultRouter()
router.register(r'qrscanlogs', QRScanLogViewSet, basename='qrscanlog')

urlpatterns = [
    path('', include(router.urls)),
    path('qrpublicscan/', QRPublicScanAPIView.as_view(), name='qrpublicscan'),
]
