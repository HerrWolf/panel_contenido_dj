from django.urls import path

from core.dashboard.views.views import HomeView, test, testAddCategory, testDeleteCategory, testSearchMovieData, \
    testSeasonInfo, testEpisodeInfo, testGetCategories

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('test/', test, name='test'),
    path('test/add-category/', testAddCategory, name='test-add-category'),
    path('test/get-categories/', testGetCategories, name='test-get-category'),
    path('test/delete-category/<int:id>/', testDeleteCategory, name='test-delete-category'),
    path('test/search/<str:content_type>/<str:query>/', testSearchMovieData, name='test-search-movie-data'),
    path('test/season/<int:series_id>/<int:season_number>/', testSeasonInfo, name='test-season-data'),
    path('test/episode/<int:series_id>/<int:season_number>/<int:episode_number>/',
         testEpisodeInfo, name='test-episode-data'),
]