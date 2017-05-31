from django.conf.urls import url
from movies import views

urlpatterns = [
    url(r'^movies/$',views.MoviesList.as_view()),
    url(r'^movies/(?P<pk>[0-9]+)/$',views.MovieDetails.as_view()),
]
