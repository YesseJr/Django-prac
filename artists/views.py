from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Artist, Song


def index(request):
    """Main page displaying all artists"""
    artists = Artist.objects.all()
    return render(request, 'artists/index.html', {'artists': artists})


def artist_detail(request, artist_id):
    """Artist detail page"""
    artist = get_object_or_404(Artist, pk=artist_id)
    songs = artist.songs.all()
    return render(request, 'artists/artist_detail.html', {
        'artist': artist,
        'songs': songs
    })


def api_artists(request):
    """API endpoint to get all artists data as JSON"""
    artists = Artist.objects.all()
    data = []
    for artist in artists:
        artist_data = {
            'id': artist.id,
            'name': artist.name,
            'genre': artist.genre,
            'bio': artist.bio,
            'imageColor': artist.image_color,
            'image': artist.image.url if artist.image else '',
            'songs': [
                {
                    'title': song.title,
                    'year': song.year,
                    'audio': song.audio.url if song.audio else ''
                }
                for song in artist.songs.all()
            ]
        }
        data.append(artist_data)
    return JsonResponse(data, safe=False)


def api_artist_detail(request, artist_id):
    """API endpoint to get single artist data"""
    artist = get_object_or_404(Artist, pk=artist_id)
    data = {
        'id': artist.id,
        'name': artist.name,
        'genre': artist.genre,
        'bio': artist.bio,
        'imageColor': artist.image_color,
        'image': artist.image.url if artist.image else '',
        'songs': [
            {
                'title': song.title,
                'year': song.year,
                'audio': song.audio.url if song.audio else ''
            }
            for song in artist.songs.all()
        ]
    }
    return JsonResponse(data)
