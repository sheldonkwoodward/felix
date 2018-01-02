from django.http import JsonResponse
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from media.models import Movie, Season
from media.forms import MovieForm, SeasonForm

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
            # TODO: fix manual time zone correction
            'date_added': str(movie.date_added - timedelta(hours=8))[:-6],
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
            # TODO: fix manual time zone correction
            'date_added': str(season.date_added - timedelta(hours=8))[:-6],
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
def media_past_minutes(request, minutes):
    oldest_date = timezone.now() - timedelta(minutes=minutes)
    movies = Movie.objects.filter(date_added__gte=oldest_date)
    seasons = Season.objects.filter(date_added__gte=oldest_date)
    return JsonResponse(search_media(request, movies, seasons))


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_past_hours(request, hours):
    oldest_date = timezone.now() - timedelta(hours=hours)
    movies = Movie.objects.filter(date_added__gte=oldest_date)
    seasons = Season.objects.filter(date_added__gte=oldest_date)
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


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_add_movie(request):

    form = MovieForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        release_year = form.cleaned_data['release_year']
        cut = form.cleaned_data['cut']
        resolution = form.cleaned_data['resolution']
        date_added = timezone.now()
        length_minutes = form.cleaned_data['length_minutes']
        path = form.cleaned_data['path']

        movie = Movie.objects.create(
            title=title,
            release_year=release_year,
            cut=cut,
            resolution=resolution,
            date_added=date_added,
            length_minutes=length_minutes,
            path=path,
        )
        movie.save()
        return JsonResponse({
            'status': 'success'
        })
    else:
        return JsonResponse({
            'status': 'failed'
        }, status=400)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def media_add_season(request):
    form = SeasonForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        season = form.cleaned_data['season']
        cut = form.cleaned_data['cut']
        resolution = form.cleaned_data['resolution']
        date_added = timezone.now()
        path = form.cleaned_data['path']

        season = Season.objects.create(
            title=title,
            season=season,
            cut=cut,
            resolution=resolution,
            date_added=date_added,
            path=path,
        )
        season.save()
        return JsonResponse({
            'status': 'success'
        })
    else:
        return JsonResponse({
            'status': 'failed'
        }, status=400)
