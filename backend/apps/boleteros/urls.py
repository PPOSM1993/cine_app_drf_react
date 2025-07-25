from rest_framework.routers import DefaultRouter
from .views import TicketOfficerViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'ticket-officers', TicketOfficerViewSet, basename='ticket-officer')

urlpatterns = [
    path('', include(router.urls)),
]
