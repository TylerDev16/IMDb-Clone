from django.urls import path
from .views import *

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('list/<int:pk>/', WatchListDetailAV.as_view(), name='watchlist_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='platform_list'),
    path('strean/<int:pk>/', StreamPlatformDetailAV.as_view(), name='platform_detail')
]
