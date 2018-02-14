from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name= 'home'

urlpatterns = [
    url(r'^$', views.index , name='index'),

#Actor:

    url(r'^actor/$', views.actor , name='actor'),
    url(r'^actor/(?P<pk>\d+)/$', views.actor_detail, name='actor_detail'),
    url(r'^actors/(?P<sel>.+?)/$', views.actors_select, name='actors_select'),

#Actress:

    url(r'^actress/$', views.actress , name='actress'),
    url(r'^actress/(?P<pk>\d+)/$', views.actress_detail, name='actress_detail'),
    url(r'^actoresses/(?P<sel>.+?)/$', views.actress_select, name='actress_select'),

#Directors:

    url(r'^directors/$', views.directors , name='directors'),
    url(r'^directors/(?P<pk>\d+)/$', views.directors_detail, name='directors_detail'),
    url(r'^director/(?P<sel>.+?)/$', views.directors_select, name='directors_select'),

#Movieslist:

    url(r'^movieslist/$', views.movieslist , name='movieslist'),
    url(r'^movieslist/(?P<pk>\d+)/$', views.movieslist_detail, name='movieslist_detail'),
    url(r'^movieslists/(?P<sel>.+?)/$', views.movieslist_select, name='movieslist_select'),

#Genres:

    url(r'^genres/$', views.genres , name='genres'),
    url(r'^genres/(?P<pk>\d+)/$', views.genres_detail, name='genres_detail'),
    url(r'^genre/(?P<sel>.+?)/$', views.genres_select, name='genres_select'),

#Rating:

    url(r'^rating/$', views.rating , name='rating'),
    url(r'^rating/(?P<pk>\d+)/$', views.rating_detail, name='rating_detail'),
    url(r'^ratings/(?P<sel>.+)/$', views.rating_select, name='rating_select'),
    url(r'^rating/(?P<sel>.+)/(?P<sel1>.+)/$', views.rating_betw, name='rating_betw'),


#Plots:
    
    url(r'^plots/$', views.plots , name='plots'),
    url(r'^plots/(?P<pk>\d+)/$', views.plots_detail, name='plots_detail'),
    url(r'^plot/(?P<sel>.+?)/$', views.plot_select, name='plot_select'),
]