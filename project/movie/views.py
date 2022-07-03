from django.shortcuts import render, redirect
from .models import Director, Movie, Review
from movie.forms import DirectorForm, MovieForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def movie_list_view(request):
    # print(request.user)
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




def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register/')
    return render(request, 'register.html', context={
        'form': form
    })
    


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, email=email,password=password)
            if user:
                login(request, user=user)
        return redirect('/login/')
    return render(request, 'login.html', context={
        'form': form
    })