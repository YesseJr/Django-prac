from django.db import models

class Artist(models.Model):
    """Model representing a music artist"""
    name = models.CharField(max_length=200, unique=True)
    genre = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='artists/', blank=True, null=True)
    image_color = models.CharField(max_length=100, default='linear-gradient(135deg, #667eea 0%, #764ba2 100%)')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Song(models.Model):
    """Model representing a song by an artist"""
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    audio = models.FileField(upload_to='songs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', 'title']

    def __str__(self):
        return f"{self.title} - {self.artist.name} ({self.year})"
