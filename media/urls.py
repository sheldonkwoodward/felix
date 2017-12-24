from django.urls import path

from . import views

urlpatterns = [
    path('movie', views.movie_all, name='movie_all'),
    path('movie/today', views.movie_today, name='movie_today'),
    path('movie/week', views.movie_week, name='movie_week')
]
