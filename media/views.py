from django.http import JsonResponse

from media.models import Movie, Season

from datetime import date, timedelta


def search_movie(movie_list, request):
    data = {
        "num": 0,
        "movies": []
    }

    for movie in movie_list:
        # TODO: add status messages for bad queries
        # TODO: use for loop instead of if statements
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
        # TODO: implement date_added search, doesn't work with normal method
        elif request.GET.get('length_minutes') is not None and str(movie.length_minutes) != request.GET.get(
                'length_minutes'):
            continue
        # TODO: implement path search, doesnt work with normal method

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

    # results info
    data['num'] = len(data['movies'])
    return data


def movie_all(request):
    movies = Movie.objects.all()
    return JsonResponse(search_movie(movies, request))


def movie_today(request):
    oldest_date = date.today() - timedelta(days=1)
    movies = Movie.objects.filter(date_added__gte=oldest_date)
    return JsonResponse(search_movie(movies, request))


def movie_week(request):
    oldest_date = date.today() - timedelta(days=7)
    movies = Movie.objects.filter(date_added__gte=oldest_date)
    return JsonResponse(search_movie(movies, request))
