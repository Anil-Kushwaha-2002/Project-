from django.urls import path
from . import views

urlpatterns = [
    path('api/data/', views.DataRecordList.as_view(), name='data-record-list'),
]
