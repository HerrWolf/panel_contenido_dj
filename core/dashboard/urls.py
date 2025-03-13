from django.urls import path

from core.dashboard.views.category.views import *
from core.dashboard.views.dashboard.views import HomeView
from core.dashboard.views.test.views import test, testAddCategory, testDeleteCategory, testSearchMovieData, \
    testSeasonInfo, testEpisodeInfo, testGetCategories

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/', category_list_view, name='category-list-view'),
    path('category/create/', category_create_view, name='category-create-view'),
    path('category/<int:pk>/edit/', category_edit_view, name='category-edit-view'),
    path('category/<int:pk>/delete/', category_delete_view, name='category-delete-view'),




    path('test/', test, name='test'),
    path('test/add-category/', testAddCategory, name='test-add-category'),
    path('test/get-categories/', testGetCategories, name='test-get-category'),
    path('test/delete-category/<int:id>/', testDeleteCategory, name='test-delete-category'),
    path('test/search/<str:content_type>/<str:query>/', testSearchMovieData, name='test-search-movie-data'),
    path('test/season/<int:series_id>/<int:season_number>/', testSeasonInfo, name='test-season-data'),
    path('test/episode/<int:series_id>/<int:season_number>/<int:episode_number>/',
         testEpisodeInfo, name='test-episode-data'),
]