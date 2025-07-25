from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Sum, F
from django.db.models.functions import TruncDate, TruncHour
from apps.tickets.models import Ticket
from apps.movies.models import Movie
from apps.authentication.models import User

from apps.seats.models import Room


class SalesAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Agrupamos tickets por fecha y sumamos los totales
        sales_data = (
            Ticket.objects.filter(status='confirmed')  # o el status que uses para venta efectiva
            .annotate(date=TruncDate('purchase_datetime'))
            .values('date')
            .annotate(total_sales=Sum('price'), total_tickets=Count('id'))
            .order_by('date')
        )

        return Response(sales_data)

# 1. Ventas por fecha
class SalesByDateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sales = (
            Ticket.objects.filter(status='confirmed')
            .annotate(date=TruncDate('purchase_datetime'))
            .values('date')
            .annotate(total_sales=Sum('price'), total_tickets=Count('id'))
            .order_by('date')
        )
        return Response(sales)

# 2. Películas más vistas
class MostViewedMoviesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        movies = (
            Ticket.objects.filter(status='confirmed')
            .values(movie_title=F('movie__title'))
            .annotate(total=Count('id'))
            .order_by('-total')[:10]
        )
        return Response(movies)

# 3. Ventas por sala
class SalesByRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rooms = (
            Ticket.objects.filter(status='confirmed')
            .values(room_name=F('room__name'))
            .annotate(total_sales=Sum('price'), total_tickets=Count('id'))
            .order_by('-total_sales')
        )
        return Response(rooms)

# 4. Distribución por horario
class SalesByHourView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        hourly_sales = (
            Ticket.objects.filter(status='confirmed')
            .annotate(hour=TruncHour('purchase_datetime'))
            .values('hour')
            .annotate(total_sales=Sum('price'), total_tickets=Count('id'))
            .order_by('hour')
        )
        return Response(hourly_sales)

# 5. Usuarios con más compras
class TopUsersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        top_users = (
            Ticket.objects.filter(status='confirmed')
            .values(user_email=F('user__email'))
            .annotate(total_tickets=Count('id'), total_spent=Sum('price'))
            .order_by('-total_spent')[:10]
        )
        return Response(top_users)

# 6. Resumen general
class SalesSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_sales = Ticket.objects.filter(status='confirmed').aggregate(
            total_amount=Sum('price'),
            total_tickets=Count('id'),
            total_users=Count('user', distinct=True)
        )
        return Response(total_sales)