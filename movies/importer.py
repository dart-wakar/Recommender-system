from csvImporter.model import CsvModel
from csvImporter.fields import IntegerField,CharField
from movies.models import Movies

class MovieCsvModel(CsvModel):
    movieId = IntegerField(match="id")
    title = CharField()
    genres = CharField()

    class Meta:
        dbModel = Movies
        delimiter = ","
