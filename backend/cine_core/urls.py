"""
URL configuration for cine_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
