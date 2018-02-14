from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Rating(models.Model):
	distribution 	 = models.CharField(max_length=500)
	votes = models.CharField(max_length=300)
	rating = models.CharField(max_length=300)
	movie_title = models.CharField(max_length=1250)

	def __str__(self):
		return self.movie_title

	def get_absolute_url(self):
		return reverse("movie:rating_detail", kwargs={"pk": self.id})


class Genres(models.Model):
	movie_title = models.CharField(max_length=2250)
	category = models.CharField(max_length=250)
	
	def __str__(self):
		return self.movie_title

	def get_absolute_url(self):
		return reverse("movie:genres_detail", kwargs={"pk": self.id})


class Plot(models.Model):
	movie_title = models.CharField(max_length=2250)
	description = models.TextField(max_length=20000)
	
	def __str__(self):
		return self.movie_title

	def get_absolute_url(self):
		return reverse("movie:plots_detail", kwargs={"pk": self.id})


class Movieslist(models.Model):
	title_with_episode 	 = models.CharField(max_length=5000)
	movie_title = models.CharField(max_length=2000)
	noo = models.CharField(max_length=500)
	episode = models.CharField(max_length=2250)
	season_id = models.CharField(max_length=225)
	nooo = models.CharField(max_length=500)
	year = models.CharField(max_length=500)

	def __str__(self):
		return self.movie_title

	def get_absolute_url(self):
		return reverse("movie:movieslist_detail", kwargs={"pk": self.id})


class Directors(models.Model):
	first_name 	 = models.CharField(max_length=350)
	last_name = models.CharField(max_length=330)
	movie_title = models.CharField(max_length=2250)
	segment = models.CharField(max_length=1250)

	def __str__(self):
		return self.movie_title

	def get_absolute_url(self):
		return reverse("movie:directors_detail", kwargs={"pk": self.id})



class Actor(models.Model):
	first_name 	 = models.CharField(max_length=350)
	last_name = models.CharField(max_length=330)
	movie_title = models.CharField(max_length=5000)
	character = models.CharField(max_length=5000)
	empty = models.CharField(max_length=5000)
	role = models.CharField(max_length=5000)

	def __str__(self):
		return self.movie_title

	def get_absolute_url(self):
		return reverse("movie:actor_detail", kwargs={"pk": self.id})



class Actress(models.Model):
	first_name 	 = models.CharField(max_length=350)
	last_name = models.CharField(max_length=330)
	movie_title = models.CharField(max_length=5000)
	character = models.CharField(max_length=5000)
	empty = models.CharField(max_length=5000)
	role = models.CharField(max_length=5000)

	def __str__(self):
		return self.movie_title

	def get_absolute_url(self):
		return reverse("movie:actress_detail", kwargs={"pk": self.id})
		