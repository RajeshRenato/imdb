# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Rating
from .models import Genres
from .models import Movieslist
from .models import Directors
from .models import Actress
from .models import Actor
from .models import Plot


# Create your views here.
def index(request):
	return render(request, 'home/index.html', { })

#Actor:

def actor(request):
	actor_list = Actor.objects.all()
	paginator = Paginator(actor_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts
	}
	return render(request, 'home/actor.html', context)

def actor_detail(request, pk):
	instance = get_object_or_404(Actor, id=pk)
	context = {
	"instance" : instance
	}
	return render(request, 'home/actor_detail.html', context)

def actors_select(request, sel):
	actors_list = Actors.objects.filter(movie_title__startswith=sel)
	paginator = Paginator(actors_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts,
	"letter":sel
	}
	return render(request, 'home/actors_select.html', context)


#Actress:

def actress(request):
	actress_list = Actress.objects.all()
	paginator = Paginator(actress_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts
	}
	return render(request, 'home/actress.html', context)

def actress_detail(request, pk):
	instance = get_object_or_404(Actress, id=pk)
	context = {
	"instance" : instance
	}
	return render(request, 'home/actress_detail.html', context)

def actress_select(request, sel):
	actress_list = Actress.objects.filter(movie_title__startswith=sel)
	paginator = Paginator(actress_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts,
	"letter":sel
	}
	return render(request, 'home/actress_select.html', context)


#Directors:

def directors(request):
	directors_list = Directors.objects.all()
	paginator = Paginator(directors_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts
	}
	return render(request, 'home/directors.html', context)

def directors_detail(request, pk):
	instance = get_object_or_404(Directors, id=pk)
	context = {
	"instance" : instance
	}
	return render(request, 'home/directors_detail.html', context)

def directors_select(request, sel):
	directors_list = Directors.objects.filter(movie_title__startswith=sel)
	paginator = Paginator(directors_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts,
	"letter":sel
	}
	return render(request, 'home/directors_select.html', context)


#Movieslist:

def movieslist(request):
	movies_list = Movieslist.objects.all()
	paginator = Paginator(movies_list, 20) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts
	}
	return render(request, 'home/movieslist.html', context)

def movieslist_detail(request, pk):
	instance = get_object_or_404(Movieslist, id=pk)
	context = {
	"instance" : instance
	}
	return render(request, 'home/movieslist_detail.html', context)

def movieslist_select(request, sel):
	movies_list = Movieslist.objects.filter(movie_title__startswith=sel)
	paginator = Paginator(movies_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts,
	"letter":sel
	}
	return render(request, 'home/movieslist_select.html', context)


#Genres:

def genres(request):
	genres_list = Genres.objects.all()
	paginator = Paginator(genres_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts
	}
	return render(request, 'home/genres.html', context)

def genres_detail(request, pk):
	instance = get_object_or_404(Genres, id=pk)
	context = {
	"instance" : instance
	}
	return render(request, 'home/genres_detail.html', context)

def genres_select(request, sel):
	genres_list = Genres.objects.filter(movie_title__startswith=sel)
	paginator = Paginator(genres_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts,
	"letter":sel
	}
	return render(request, 'home/genres_select.html', context)



#Rating:

def rating(request):
	alp =['1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0','2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9','3.0','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9','4.0','4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8','4.9','5.0','5.1','5.2','5.3','5.4','5.5','5.6','5.7','5.8','5.9','6.0','6.1','6.2','6.3','6.4','6.5','6.6','6.7','6.8','6.9','7.0','7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8','7.9','8.0','8.1','8.2','8.3','8.4','8.5','8.6','8.7','8.8','8.9','9.0','9.1','9.2','9.3','9.4','9.5','9.6','9.7','9.8','9.9','10.0']
	rating_list = Rating.objects.all()
	paginator = Paginator(rating_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts,
	"alp":alp
	}
	return render(request, 'home/rating.html', context)

def rating_detail(request, pk):
	alp =['1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0','2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9','3.0','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9','4.0','4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8','4.9','5.0','5.1','5.2','5.3','5.4','5.5','5.6','5.7','5.8','5.9','6.0','6.1','6.2','6.3','6.4','6.5','6.6','6.7','6.8','6.9','7.0','7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8','7.9','8.0','8.1','8.2','8.3','8.4','8.5','8.6','8.7','8.8','8.9','9.0','9.1','9.2','9.3','9.4','9.5','9.6','9.7','9.8','9.9','10.0']
	instance = get_object_or_404(Rating, id=pk)
	context = {
	"instance" : instance,
	"alp":alp
	}
	return render(request, 'home/rating_detail.html', context)

def rating_select(request, sel):
	rating_list= ""
	alp =['1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0','2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9','3.0','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9','4.0','4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8','4.9','5.0','5.1','5.2','5.3','5.4','5.5','5.6','5.7','5.8','5.9','6.0','6.1','6.2','6.3','6.4','6.5','6.6','6.7','6.8','6.9','7.0','7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8','7.9','8.0','8.1','8.2','8.3','8.4','8.5','8.6','8.7','8.8','8.9','9.0','9.1','9.2','9.3','9.4','9.5','9.6','9.7','9.8','9.9','10.0']
	sel=float(sel)
	print sel
	rating_list = Rating.objects.filter(rating=sel).order_by('rating')
	paginator = Paginator(rating_list, 20)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts,
	"rating":sel,
	"alp":alp
	}
	return render(request, 'home/rating_select.html', context)

def rating_betw(request, sel, sel1):
	print sel
	alp =['1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0','2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9','3.0','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9','4.0','4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8','4.9','5.0','5.1','5.2','5.3','5.4','5.5','5.6','5.7','5.8','5.9','6.0','6.1','6.2','6.3','6.4','6.5','6.6','6.7','6.8','6.9','7.0','7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8','7.9','8.0','8.1','8.2','8.3','8.4','8.5','8.6','8.7','8.8','8.9','9.0','9.1','9.2','9.3','9.4','9.5','9.6','9.7','9.8','9.9','10.0']
	# sel=float(sel)
	# sel1=float(sel1)
	rating_list = Rating.objects.filter(rating__range=(sel,sel1)).order_by('rating')
	rate_list = rating_list
	paginator = Paginator(rate_list, 25)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts,
	"rating":sel,
	"alp":alp
	}
	return render(request, 'home/rating_select.html', context)


#Plots:

def plots(request):
	plot_list = Plot.objects.all()
	paginator = Paginator(plot_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts
	}
	return render(request, 'home/plots.html', context)

def plots_detail(request, pk):
	instance = get_object_or_404(Rating, id=pk)
	context = {
	"instance" : instance
	}
	return render(request, 'home/plots_detail.html', context)

def plot_select(request, sel):
	plot_list = Plot.objects.filter(movie_title__startswith=sel)
	paginator = Paginator(plot_list, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
	"object_list" : posts,
	"letter":sel
	}
	return render(request, 'home/plot_select.html', context)
