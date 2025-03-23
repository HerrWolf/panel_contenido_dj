from django.urls import path

from core.dashboard.views.category.views import *
from core.dashboard.views.dashboard.views import HomeView
from core.dashboard.views.movie.views import *
from core.dashboard.views.test.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/', category_list_view, name='category-list-view'),
    path('category/create/', category_create_view, name='category-create-view'),
    path('category/<int:pk>/edit/', category_edit_view, name='category-edit-view'),
    path('category/<int:pk>/delete/', category_delete_view, name='category-delete-view'),
    path('movie/', movie_list_view, name='movie-list-view'),
    path('movie/fetch/', fetch_movie_by_id, name='fetch-movie-by-id'),
    path('movie/search/', search_movies_by_title, name='search-movies-by-title'),
    path('movie/create/', movie_create_view, name='movie-create-view'),
    path('movie/<int:pk>/edit/', movie_edit_view, name='movie-edit-view'),
    path('movie/<int:pk>/delete/', movie_delete_view, name='movie-delete-view'),




    path('test/', test, name='test'),
    path('test/add-category/', testAddCategory, name='test-add-category'),
    path('test/get-categories/', testGetCategories, name='test-get-category'),
    path('test/delete-category/<int:id>/', testDeleteCategory, name='test-delete-category'),
    path('test/search/<str:content_type>/<str:query>/', testSearchMovieData, name='test-search-movie-data'),
    path('test/season/<int:series_id>/<int:season_number>/', testSeasonInfo, name='test-season-data'),
    path('test/episode/<int:series_id>/<int:season_number>/<int:episode_number>/',
         testEpisodeInfo, name='test-episode-data'),
    path('test/peliculas_contenido_fuss/', test_get_contenido_fuss_movies, name='test-get-contenido-movies'),
]