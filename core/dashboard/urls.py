from django.urls import path

from core.dashboard.views.views import HomeView, test

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('test/', test, name='test'),
]