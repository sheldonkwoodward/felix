from django.http import HttpResponse, JsonResponse

from media.models import Movie, Season


def index(request):
    return HttpResponse("Media index.")


def query_movie(request):
    all_movies = Movie.objects.all()
    data = {
        "status": [],
        "results": []
    }

    for movie in all_movies:
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
        data['results'].append(single_json)
    return JsonResponse(data)


# TODO: implement query_season
def query_season(request):
    return JsonResponse({
        "status": [],
        "results": []
    })
