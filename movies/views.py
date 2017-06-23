from movies.models import Movies,Preferences
from movies.serializers import MovieSerializer,UserSerializer,PreferenceSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from movies.utils import recommender
from django.contrib.auth.models import User

# Create your views here.

class MoviesList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MovieSerializer
    def get_queryset(self):
        queryset = Movies.objects.all()
        searchparam = self.request.query_params.get('searchkey',None)
        if searchparam is not None:
            queryset = queryset.filter(title__icontains=searchparam)
        return queryset

class MovieDetails(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class MoviesListRetrieve(APIView):
    def post(self,request,format=None):
        pk_list = request.data['ids']
        if pk_list:
            movies = Movies.objects.filter(pk__in=pk_list)
        else:
            movies = Movies.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)

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

class UserRegister(APIView):
    permission_classes = (AllowAny,)
    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUser(APIView):
    def get(self,request,format=None):
        currentuser = self.request.user
        serializer = UserSerializer(currentuser)
        return Response(serializer.data)

class PreferenceCreate(generics.CreateAPIView):
    queryset = Preferences.objects.all()
    serializer_class = PreferenceSerializer
    def perform_create(self,serializer):
        user_id = self.request.user.id
        print user_id
        user = User.objects.get(pk=user_id)
        serializer.save(user=user)

class PreferencesList(generics.ListAPIView):
    queryset = Preferences.objects.all()
    serializer_class = PreferenceSerializer

class PreferencesListRetrieve(APIView):
    def post(self,request,format=None):
        pk_list = request.data['ids']
        if pk_list:
            preferences = Preferences.objects.filter(pk__in=pk_list)
        else:
            preferences = Preferences.objects.all()
        serializer = PreferenceSerializer(preferences,many=True)
        return Response(serializer.data)
