from django.http import JsonResponse
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from media.models import Movie, Season, Episode
from media.forms import MovieForm, SeasonForm, EpisodeForm

from datetime import datetime, date, timedelta


TokenAuthentication.keyword = 'Bearer'

@api_view(['GET'])
def test_req(request):
    return JsonResponse({'success': 'yes!'})