from movies.models import Movies
from movies.serializers import MovieSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from movies.utils import recommender

# Create your views here.

class MoviesList(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class MovieDetails(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class MovieRecommendations(APIView):
    def post(self,request,format=None):
        movie_id = request.data['id']
        recommended_movie_ids = recommender(movie_id)
        if recommended_movie_ids:
            print recommended_movie_ids
            recommended_movies = Movies.objects.filter(pk__in=recommended_movie_ids)
        else:
            recommended_movies = Movies.objects.all()
        serializer = MovieSerializer(recommended_movies,many=True)
        return Response(serializer.data)
