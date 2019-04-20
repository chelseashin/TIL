# from django.shortcuts import reverse
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    score_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='score_movies', through='Score')
    
    # def get_absolute_url(self):
    #     return reverse("movies:detail", args=[self.pk])
    
    def __str__(self):
        return self.title
    
class Score(models.Model):
    content = models.CharField(max_length=140)
    # value = models.IntegerField()
    value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
        
    class Meta:
        ordering = ['-value']