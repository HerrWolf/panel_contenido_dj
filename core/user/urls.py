from django.urls import path
from core.user.views import UserListView, UserCreateView

urlpatterns = [
    path('list/', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='user_create'),
]
