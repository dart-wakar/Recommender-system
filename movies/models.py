from __future__ import unicode_literals

from django.db import models
from csvImporter.model import CsvDbModel

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
