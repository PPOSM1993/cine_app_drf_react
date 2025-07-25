# promotions/views.py
from rest_framework import viewsets, permissions
from .models import Promotion
from .serializers import PromotionSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import PromotionFilter


class PublicPromotionListView(ListAPIView):
    serializer_class = PromotionSerializer
    pagination_class = None

    def get_queryset(self):
        now = timezone.now()
        return Promotion.objects.filter(
            is_active=True,
            start_date__lte=now,
            end_date__gte=now
        )
class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PromotionFilter
    search_fields = ["title", "description", "code"]
    ordering_fields = ["start_date", "end_date", "created_at", "discount_value"]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class ActivePromotionsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        now = timezone.now()
        promotions = Promotion.objects.filter(
            is_active=True,
            start_date__lte=now,
            end_date__gte=now
        ).exclude(
            usage_limit__isnull=False,
            used_count__gte=models.F('usage_limit')
        )

        serializer = PromotionSerializer(promotions, many=True)
        return Response(serializer.data)