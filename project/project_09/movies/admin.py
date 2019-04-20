from django.contrib import admin
from .models  import Genre, Movie

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'poster_url', 'description', 'genre_id',)
admin.site.register(Movie, MovieAdmin)