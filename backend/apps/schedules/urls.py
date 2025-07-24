from rest_framework.routers import DefaultRouter
from .views import ScheduleViewSet

from django.urls import path, include

router = DefaultRouter()
router.register(r'', ScheduleViewSet, basename='schedules')

urlpatterns = [
    path('', include(router.urls)),
]
