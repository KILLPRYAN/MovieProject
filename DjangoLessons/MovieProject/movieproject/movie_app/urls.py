from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name="movie_detail"),
    path('directors', views.show_directors),
    path('directors/<int:director.index>', views.info_director),
    path('actors', views.show_actors),
    path('actors/<int:actor.index>', views.info_actors)

]