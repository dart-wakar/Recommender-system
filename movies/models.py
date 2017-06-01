from __future__ import unicode_literals

from django.db import models
from csvImporter.model import CsvDbModel
from django.contrib.auth.models import User

# Create your models here.

#class MovieCsvModel(CsvDbModel):
#    movieId = IntegerField(match="id")
#    title = CharField()
#    genres = CharField()

#    class Meta:
#        dbModel = Movies
#        delimiter = ","

class Movies(models.Model):
    title = models.CharField(max_length=100,blank=True)
    details = models.CharField(max_length=250,blank=True)
    genres = models.CharField(max_length=100,blank=True)

    class Meta:
        ordering = ('id',)

class Preferences(models.Model):
    movie_id = models.IntegerField()
    user = models.ForeignKey(User,related_name='preferences',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    rating = models.FloatField()

    class Meta:
        ordering = ('created',)
