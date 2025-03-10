from django.urls import path
from core.user.views import *
urlpatterns = [
    # path('list/', UserListView.as_view(), name='user_list'),
    path('list/', user_list_view, name='user_list'),
    path('<int:pk>/edit/', user_edit_view, name='user_edit'),
    path('<int:pk>/delete/', user_delete_view, name='user_delete'),
]

