from django.conf.urls import url
from movies import views

urlpatterns = [
    url(r'^movies/$',views.MoviesList.as_view()),
    url(r'^movies/(?P<pk>[0-9]+)/$',views.MovieDetails.as_view()),
    url(r'^movies/list/$',views.MoviesListRetrieve.as_view()),
    url(r'^recommendedmovies/$',views.MovieRecommendations.as_view()),
    url(r'^users/register/$',views.UserRegister.as_view()),
    url(r'^users/$',views.UsersList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetails.as_view()),
    url(r'^currentuser/$',views.CurrentUser.as_view()),
    url(r'^preferences/create/$',views.PreferenceCreate.as_view()),
    url(r'^preferences/$',views.PreferencesList.as_view()),
    url(r'^preferences/list/$',views.PreferencesListRetrieve.as_view()),
]
