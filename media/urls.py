from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie', views.query_movie, name='query_movie'),
    path('season', views.query_season, name='query_season')
]
