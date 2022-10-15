from django.contrib import admin
from .models import Artist
from albums.models import Album
# Register your models here.

class AlbumInline(admin.TabularInline):
    model = Album

    def get_extra(self, request, obj=None, **kwargs):
        return 0

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("stage_name", "social_link", "approved_albums")


    inlines = [
        AlbumInline,
    ]

    


