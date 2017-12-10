from django.db import models
import uuid


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=250, blank=False)
    release_year = models.IntegerField(blank=False)
    cut = models.CharField(max_length=250)
    resolution = models.CharField(max_length=250, blank=False)
    date_added = models.DateField(blank=False)
    length_minutes = models.IntegerField(blank=False)
    path = models.TextField(blank=False)


class Season(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=250, blank=False)
    season = models.IntegerField(blank=False)
    cut = models.CharField(max_length=250)
    resolution = models.CharField(max_length=250, blank=False)
    date_added = models.DateField(blank=False)
    path = models.TextField(blank=False)
