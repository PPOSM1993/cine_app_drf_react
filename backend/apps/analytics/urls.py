from django.urls import path
from .views import (
    SalesByDateView,
    MostViewedMoviesView,
    SalesByRoomView,
    SalesByHourView,
    TopUsersView,
    SalesSummaryView,
)

urlpatterns = [
    path('sales/', SalesByDateView.as_view(), name='analytics-sales-date'),
    path('movies/', MostViewedMoviesView.as_view(), name='analytics-most-viewed-movies'),
    path('rooms/', SalesByRoomView.as_view(), name='analytics-sales-room'),
    path('hours/', SalesByHourView.as_view(), name='analytics-sales-hour'),
    path('top-users/', TopUsersView.as_view(), name='analytics-top-users'),
    path('summary/', SalesSummaryView.as_view(), name='analytics-summary'),
]
