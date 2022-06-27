from django.shortcuts import render, redirect
from .models import Director, Movie, Review
from movie.forms import DirectorForm, MovieForm

# Create your views here.

def movie_list_view(request):
    context = {
        'movie_list': Movie.objects.all(),
        'director_list': Director.objects.all()
    }
    return render(request, "movie.html", context=context)


def movie_detail_view(request, id):
    # movies = Movie.objects.prefetch_related('rewiews').get(id=id)
    movies = Movie.objects.get(id=id)
    context = {
        'movie_detail': movies,
        'reviews': Review.objects.filter(movie=movies)
    }
    return render(request, 'detail.html', context=context)


def add_director_view(request):
    form = DirectorForm()
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movies/')
    return render(request, 'add_director.html', context={
        'form': form
    })

def add_movie_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movies/')
    return render(request, 'add_movie.html', context={
        'form': form
    })
