from django.urls import path
from .views import UserListView  # Import a dummy view to prevent errors

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
]
