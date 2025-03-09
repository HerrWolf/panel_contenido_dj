from django.urls import path
from core.user.views import *
urlpatterns = [
    # path('list/', UserListView.as_view(), name='user_list'),
    path('list/', user_list_view, name='user_list'),
    # path('add/', UserCreateView.as_view(), name='user_create'),
]

