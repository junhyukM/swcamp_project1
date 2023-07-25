from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_movie, name='create_movie'),
    path('<int:pk>/', views.movie_detail, name='movie_detail'),
    path('<int:pk>/update/', views.update_movie, name='update_movie'),
    path('<int:pk>/delete/', views.delete_movie, name='delete_movie'),
]
