from django.urls import path
from .views import InsightAPI

urlpatterns = [
    path('api/insights/', InsightAPI.as_view(), name='insight-api'),
]
