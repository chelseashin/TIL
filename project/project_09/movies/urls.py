from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_pk>/scores/<int:score_pk>/delete/', views.score_delete, name='score_delete'),
    path('<int:movie_pk>/scores/new/', views.score_create, name='score_create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('', views.list, name='list'),
]
