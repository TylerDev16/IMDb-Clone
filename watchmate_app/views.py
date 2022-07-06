from django.shortcuts import render
from watchmate_app.models import Movie
from django.http import JsonResponse

# Create your views here.


# display movie list
def movie_list(request):
    movies = Movie.objects.all()
    data = {'movies': list(movies.values())}

    return JsonResponse(data)


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
    }
    return JsonResponse(data)