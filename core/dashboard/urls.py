from django.urls import path

from core.dashboard.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]