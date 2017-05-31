from movies.models import Movies
from movies.serializers import MovieSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.

class MoviesList(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class MovieDetails(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
