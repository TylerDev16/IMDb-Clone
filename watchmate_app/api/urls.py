from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# 1 url handles for list and detail
router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='movie-detail'),

    # path for router
    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name='streamplatform-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

]
