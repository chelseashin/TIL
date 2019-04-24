from rest_framework import serializers
from .models import Genre, Movie, Score

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name',]
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience', 'poster_url', 'description', 'genre']
        
class GenreDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(source ='movie_set', many=True)
    movie_count = serializers.IntegerField(source='movie_set.count')
    class Meta:
        model = Genre
        fields = ['id', 'movies', 'name', 'movie_count']

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ['id', 'title', 'audience', 'poster_url', 'description', 'genre']
        field = ['__all__']
        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'score', 'content',]