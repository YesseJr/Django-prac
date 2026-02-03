from django.urls import path
from . import views

app_name = 'artists'

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('api/artists/', views.api_artists, name='api_artists'),
    path('api/artist/<int:artist_id>/', views.api_artist_detail, name='api_artist_detail'),
]
