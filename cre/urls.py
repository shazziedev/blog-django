from django.urls import path
from .views import *

app_name = 'articles'

urlpatterns = [
    path('<int:pk>/<str:slug>/',postDetails.as_view(template_name='post/details.html' ),name="post-details"),
    path('music/',MusicScreen.as_view(),name="music-list"),
    path('movies/',MovieScreen.as_view(),name="movies-list"),
    path('videos/',VideoScreen.as_view(),name="videos-list"),
    path('series/',SerrieScreen.as_view(),name="serries-list"),
    path('add/',AddPostScreen.as_view(),name="add-post"),
    path('search/',SearchScreen.as_view(),name="search"),
]