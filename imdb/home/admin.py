from __future__ import unicode_literals
from .models import Rating, Genres, Plot, Directors, Movieslist, Actor, Actress
from django.contrib import admin

# Register your models here.

class AdminRating(admin.ModelAdmin):
	list_display = ['movie_title','rating']
	# list_display_links = ['updated']
	list_filter = ['rating']
	search_fields = ['movie_title']
	class Meta:
		model = Rating

class AdminGenres(admin.ModelAdmin):
	list_display = ['movie_title','category']
	list_filter = ['category']
	search_fields = ['movie_title']
	class Meta:
		model = Genres

class AdminPlot(admin.ModelAdmin):
	# list_filter = ['category']
	search_fields = ['movie_title']
	class Meta:
		model = Plot

class AdminMovieslist(admin.ModelAdmin):
	list_display = ['movie_title','year']
	# list_filter = ['category']
	search_fields = ['movie_title']
	class Meta:
		model = Movieslist

class AdminDirectors(admin.ModelAdmin):
	list_display = ['first_name','movie_title']
	# list_filter = ['category']
	search_fields = ['movie_title']
	class Meta:
		model = Directors

class AdminActor(admin.ModelAdmin):
	list_display = ['first_name','movie_title']
	# list_filter = ['category']
	search_fields = ['movie_title']
	class Meta:
		model = Actor


class AdminActress(admin.ModelAdmin):
	list_display = ['first_name','movie_title']
	# list_filter = ['category']
	search_fields = ['movie_title']
	class Meta:
		model = Actress

admin.site.register(Rating, AdminRating)
admin.site.register(Genres, AdminGenres)
admin.site.register(Plot, AdminPlot)
admin.site.register(Movieslist, AdminMovieslist)
admin.site.register(Directors, AdminDirectors)
admin.site.register(Actor, AdminActor)
admin.site.register(Actress, AdminActress)
# admin.site.register(Genres, AdminGenres)