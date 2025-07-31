


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authentication/', include('apps.authentication.urls')),
    path('api/movies/', include('apps.movies.urls')),
    path('api/seats/', include('apps.seats.urls')),
    path('api/schedules/', include('apps.schedules.urls')),
    path('api/reservations/', include('apps.reservations.urls')),
    path('api/tickets/', include('apps.tickets.urls')),
    path('api/payments/', include('apps.payments.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path('api/support/', include('apps.support.urls')),
    path('api/analytics/', include('apps.analytics.urls')),
    path('api/fidelizacion/', include('apps.fidelizacion.urls')),
    path('api/promotions/', include('apps.promotions.urls')),
    path('api/boleteros/', include('apps.boleteros.urls')),
    path('api/qrscanner', include('apps.qrscanner.urls')),
    path('api/cinema/', include('apps.cinema.urls'))
]
