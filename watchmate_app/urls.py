from django.urls import path
from .views import *

urlpatterns = [
    path('list/', movie_list, name='movie_list'),
    path('<int:pk>/', movie_detail, name='movie_detail')
]
