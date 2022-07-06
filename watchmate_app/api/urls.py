from django.urls import path
from .views import *

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='streamplatform-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail')
]
