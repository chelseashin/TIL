from django.contrib import admin
from .models import Genre, Movie

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'poster_url', 'description', 'genre')
    
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)