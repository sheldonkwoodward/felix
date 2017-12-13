from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('query/movie', views.query_movie, name='query_movie'),
    path('query/season', views.query_season, name='query_season')
]
