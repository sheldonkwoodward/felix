from django.urls import path

from . import views

urlpatterns = [
    path('', views.media_all, name='media_all'),
    path('<int:year>/<int:month>/<int:day>', views.media_date_day, name='media_date_day'),
    path('<int:year>/<int:month>', views.media_date_month, name='media_date_month'),
    path('<int:year>', views.media_date_year, name='media_date_year'),
    path('days/<int:days>', views.media_past_days, name='media_past_days'),
    path('weeks/<int:weeks>', views.media_past_weeks, name='media_past_weeks'),
    path('months/<int:months>', views.media_past_months, name='media_past_months'),
    path('years/<int:years>', views.media_past_years, name='media_past_years'),
]
