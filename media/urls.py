from django.urls import path

from . import views

urlpatterns = [
    path('movie', views.movie_all, name='movie_all'),
    path('today', views.movie_today, name='movie_today'),
    path('week', views.movie_week, name='movie_week')
]
