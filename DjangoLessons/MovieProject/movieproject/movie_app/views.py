from urllib import request

from django.shortcuts import render, get_object_or_404
from .models import Movie
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
    li_elements = ''
    # for director in


def info_director(request):
    return render(request, 'movie_app/info_director.html')


def show_actors(request):
    return render(request, 'movie_app/all_actors.html')


def info_actor(request):
    return render(request, 'movie_app/info_actor.html')
