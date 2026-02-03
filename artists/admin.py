from django.contrib import admin
from .models import Artist, Song


class SongInline(admin.TabularInline):
    """Inline admin for songs"""
    model = Song
    extra = 1
    fields = ('title', 'year', 'audio')


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Admin configuration for Artist model"""
    list_display = ('name', 'genre', 'created_at')
    search_fields = ('name', 'genre')
    list_filter = ('genre', 'created_at')
    inlines = [SongInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'genre', 'bio')
        }),
        ('Visual', {
            'fields': ('image', 'image_color')
        }),
    )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """Admin configuration for Song model"""
    list_display = ('title', 'artist', 'year', 'created_at')
    search_fields = ('title', 'artist__name')
    list_filter = ('year', 'artist', 'created_at')
    ordering = ('-year', 'title')
