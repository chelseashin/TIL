from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Movie, Score
from .forms import ScoreForm

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies, 
    }
    return render(request, 'movies/list.html', context)
    
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ScoreForm()
    context = {
        'movie' : movie, 
        'form' : form,
    }
    return render(request, 'movies/detail.html', context)
    
@require_POST
@login_required
def score_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ScoreForm(require_POST)
    if form.is_valid():
        score = form.save(commit=False)
        score.user = request.user
        score_movie_id = movie_pk
        score.save()
    return redirect('movies:detail', movie_pk)
    # else:
    #     return redirect('movies:detail', movie_pk)

@require_POST
@login_required        
def score_delete(request, movie_pk, score_pk):
    score = get_object_or_404(Score, pk=score_pk)
    score.delete()
    return redirect('movies:detail', movie_pk)