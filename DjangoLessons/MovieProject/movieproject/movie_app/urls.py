from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name="movie_detail"),
    path('directors/', views.show_directors),
    path('directors/<int:id_director>', views.info_director, name='director_detail'),
    path('actors', views.show_actors),
    path('actors/<int:id_actor>', views.info_actor, name='actor_detail')

]