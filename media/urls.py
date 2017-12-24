from django.urls import path

from . import views

urlpatterns = [
    path('movie', views.movie_all, name='movie_all'),
    path('movie/days/<int:days>', views.movie_days, name='movie_days'),
    path('movie/weeks/<int:weeks>', views.movie_weeks, name='movie_weeks'),
    path('movie/months/<int:months>', views.movie_months, name='movie_months'),
    path('movie/years/<int:years>', views.movie_years, name='movie_years'),
]
