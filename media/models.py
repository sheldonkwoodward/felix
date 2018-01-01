from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Movie(models.Model):
    title = models.CharField(max_length=250, blank=False)
    release_year = models.IntegerField(blank=False)
    cut = models.CharField(max_length=250)
    resolution = models.CharField(max_length=250, blank=False)
    date_added = models.DateTimeField(blank=False)
    length_minutes = models.IntegerField(blank=False)
    path = models.TextField(blank=False)

    def __str__(self):
        return self.title


class Season(models.Model):
    title = models.CharField(max_length=250, blank=False)
    season = models.IntegerField(blank=False)
    cut = models.CharField(max_length=250)
    resolution = models.CharField(max_length=250, blank=False)
    date_added = models.DateTimeField(blank=False)
    path = models.TextField(blank=False)

    def __str__(self):
        return self.title
