from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from media.models import Movie, Season

from datetime import datetime, date, timedelta


TokenAuthentication.keyword = 'Bearer'


def search_media(request, movie_list, season_list):
    data = {
        "time_stamp": "2000-01-01 00:00:00.000000",
        "movie_num": 0,
        "season_num": 0,
        "movies": [],
        "seasons": []
    }

    # find movies
    for movie in movie_list:
        if request.GET.get('id') is not None and str(movie.id) != request.GET.get('id'):
            continue
        elif request.GET.get('title') is not None and movie.title not in request.GET.get('title'):
            continue
        elif request.GET.get('release_year') is not None and str(movie.release_year) != request.GET.get('release_year'):
            continue
        elif request.GET.get('cut') is not None and movie.cut not in request.GET.get('cut'):
            continue
        elif request.GET.get('resolution') is not None and movie.resolution not in request.GET.get('resolution'):
            continue
        elif request.GET.get('length_minutes') is not None and str(movie.length_minutes) != request.GET.get(
                'length_minutes'):
            continue
        elif request.GET.get('season') is not None:
            continue

        single_json = {
            'id': movie.id,
            'title': movie.title,
            'release_year': movie.release_year,
            'cut': movie.cut,
            'resolution': movie.resolution,
            'date_added': movie.date_added,
            'length_minutes': movie.length_minutes,
            'path': movie.path,
        }
        data['movies'].append(single_json)

    # find seasons
    for season in season_list:
        if request.GET.get('id') is not None and str(season.id) != request.GET.get('id'):
            continue
        elif request.GET.get('title') is not None and season.title not in request.GET.get('title'):
            continue
        elif request.GET.get('season') is not None and str(season.season) != request.GET.get('season'):
            continue
        elif request.GET.get('cut') is not None and season.cut not in request.GET.get('cut'):
            continue
        elif request.GET.get('resolution') is not None and season.resolution not in request.GET.get('resolution'):
            continue
        elif request.GET.get('length_minutes') is not None:
            continue

        single_json = {
            'id': season.id,
            'title': season.title,
            'season': season.season,
            'cut': season.cut,
            'resolution': season.resolution,
            'date_added': season.date_added,
            'path': season.path,
        }
        data['seasons'].append(single_json)

    # results info
    data['time_stamp'] = str(datetime.now())
    data['movie_num'] = len(data['movies'])
    data['season_num'] = len(data['seasons'])
    return data


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_all(request):
    print('GET ALL MEDIA')
    movies = Movie.objects.all()
    seasons = Season.objects.all()
    return JsonResponse(search_media(request, movies, seasons))


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_date_day(request, year, month, day):
    movies = Movie.objects.filter(date_added__year=year).filter(date_added__month=month).filter(date_added__day=day)
    seasons = Season.objects.filter(date_added__year=year).filter(date_added__month=month).filter(date_added__day=day)
    return JsonResponse(search_media(request, movies, seasons))


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_date_month(request, year, month):
    movies = Movie.objects.filter(date_added__year=year).filter(date_added__month=month)
    seasons = Season.objects.filter(date_added__year=year).filter(date_added__month=month)
    return JsonResponse(search_media(request, movies, seasons))


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_date_year(request, year):
    movies = Movie.objects.filter(date_added__year=year)
    seasons = Season.objects.filter(date_added__year=year)
    return JsonResponse(search_media(request, movies, seasons))


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_past_days(request, days):
    oldest_date = date.today() - timedelta(days=days)
    movies = Movie.objects.filter(date_added__gte=oldest_date)
    seasons = Season.objects.filter(date_added__gte=oldest_date)
    return JsonResponse(search_media(request, movies, seasons))


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_past_weeks(request, weeks):
    oldest_date = date.today() - timedelta(days=weeks * 7)
    movies = Movie.objects.filter(date_added__gte=oldest_date)
    seasons = Season.objects.filter(date_added__gte=oldest_date)
    return JsonResponse(search_media(request, movies, seasons))


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_past_months(request, months):
    oldest_date = date.today() - timedelta(days=months * 31)
    movies = Movie.objects.filter(date_added__gte=oldest_date)
    seasons = Season.objects.filter(date_added__gte=oldest_date)
    return JsonResponse(search_media(request, movies, seasons))


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_past_years(request, years):
    oldest_date = date.today() - timedelta(days=years * 365)
    movies = Movie.objects.filter(date_added__gte=oldest_date)
    seasons = Season.objects.filter(date_added__gte=oldest_date)
    return JsonResponse(search_media(request, movies, seasons))
