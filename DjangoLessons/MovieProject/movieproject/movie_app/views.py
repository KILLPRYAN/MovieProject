from urllib import request

from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


# Create your views here.

def show_all_movie(request):
    # movies = Movie.objects.order_by(F('rating').asc(nulls_last=True), 'rating')
    movies = Movie.objects.annotate(
        new_field_bool=Value(True),
        new_budget=F('budget') + 100,
        fff=F('rating') * F('year'),
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_directors(request):
    directors = Director.objects.all()
    return render(request, "movie_app/all_directors.html", context={
        'directors': directors
    })


def info_director(request, id_director: int):
    dir = get_object_or_404(Director, id=id_director)
    return render(request, "movie_app/one_director.html", context={
        'dir': dir,
    })


def show_actors(request):
    actors = Actor.objects.all()
    return render(request, "movie_app/all_actors.html", context={
        'actors': actors
    })


def info_actor(request, id_actor: int):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, "movie_app/one_actor.html", context={
        'actor': actor
    })
