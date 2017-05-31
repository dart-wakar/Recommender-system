from rest_framework import serializers
from movies.models import Movies

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('id','title','details','genres')
