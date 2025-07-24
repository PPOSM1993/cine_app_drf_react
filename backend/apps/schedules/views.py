from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import date, timedelta

from .models import Schedule
from .serializers import ScheduleSerializer, ScheduleListSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().select_related('movie', 'room')
    serializer_class = ScheduleSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'today', 'by_date', 'by_movie', 'calendar']:
            return ScheduleListSerializer
        return ScheduleSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        movie_id = self.request.query_params.get('movie_id')
        room_id = self.request.query_params.get('room_id')
        date_str = self.request.query_params.get('date')

        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)

        if room_id:
            queryset = queryset.filter(room_id=room_id)

        if date_str:
            try:
                filter_date = date.fromisoformat(date_str)
                queryset = queryset.filter(day=filter_date)
            except ValueError:
                pass  # o puedes lanzar un error 400

        return queryset.order_by('date', 'start_time')

    @action(detail=False, methods=['get'])
    def today(self, request):
        today = timezone.localdate()
        schedules = self.get_queryset().filter(day=today)
        serializer = self.get_serializer(schedules, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_date(self, request):
        date_str = request.query_params.get('date')
        if not date_str:
            return Response({"detail": "Se requiere el parámetro 'date'."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            target_date = date.fromisoformat(date_str)
        except ValueError:
            return Response({"detail": "Formato de fecha inválido. Usa YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        schedules = self.get_queryset().filter(day=target_date)
        serializer = self.get_serializer(schedules, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_movie(self, request):
        movie_id = request.query_params.get('movie_id')
        if not movie_id:
            return Response({"detail": "Se requiere el parámetro 'movie_id'."}, status=status.HTTP_400_BAD_REQUEST)

        schedules = self.get_queryset().filter(movie_id=movie_id)
        serializer = self.get_serializer(schedules, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def calendar(self, request):
        """
        Devuelve un diccionario con las fechas como claves y los horarios como lista de valores.
        Ideal para construir una vista tipo calendario.
        """
        queryset = self.get_queryset()
        calendar_data = {}

        for schedule in queryset:
            day_str = schedule.day.strftime("%Y-%m-%d")
            if day_str not in calendar_data:
                calendar_data[day_str] = []
            calendar_data[day_str].append(ScheduleListSerializer(schedule).data)

        return Response(calendar_data)
