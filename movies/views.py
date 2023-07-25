from django.shortcuts import render, redirect, get_object_or_404 
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
# Create your views here.



def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm()
    return render(request, 'movies/create_movie.html', {'form': form})

def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/update_movie.html', {'form': form, 'movie': movie})

def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('index')
    return render(request, 'movies/delete_movie.html', {'movie': movie})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return redirect('movie_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'form': form})
