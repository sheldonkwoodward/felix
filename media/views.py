from django.http import HttpResponse, JsonResponse

from media.models import Movie, Season


def index(request):
    return HttpResponse("Media index.")


def query_movie(request):
    all_movies = Movie.objects.all()
    data = {"results": []}
    for movie in all_movies:
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
        data['results'].append(single_json)
    return JsonResponse(data)


def query_season(request):
    all_seasons = Season.objects.all()
    data = {"results": []}
    for season in all_seasons:
        single_json = {
            'id': season.id,
            'title': season.title,
            'season': season.season,
            'cut': season.cut,
            'resolution': season.resolution,
            'date_added': season.date_added,
            'path': season.path,
        }
        data['results'].append(single_json)
    return JsonResponse(data)
