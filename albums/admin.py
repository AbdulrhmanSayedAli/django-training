from django.contrib import admin
from .models import Album , Song
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages

class SongsFormSet (forms.BaseInlineFormSet):
    def getSongsCount(self):
        count = 0
        for form in self.forms:
            if not form.cleaned_data["DELETE"]:
                count+=1
        return count


    def clean(self):
        super().clean()
        if self.getSongsCount() == 0 :
            raise ValidationError("album should have at least one song")



class SongInline(admin.TabularInline):
    model = Song
    formset = SongsFormSet
    def get_extra(self, request, obj=None, **kwargs):
        return 0


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')
    list_display = ("name", "is_approved")
    inlines = [
        SongInline,
    ]
    


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    readonly_fields = ('thumbnail',)

    def delete_model(modeladmin, request, song):
        if song.album.songs.count() == 1:
            messages.add_message(request, messages.ERROR, 'you cant delete this song because every album should have at least one song')
        else :
            song.delete()

    def delete_queryset(modeladmin, request, queryset):
        albums = {}
        has_error = False
        for song in queryset:
            album = song.album 
            if not album.id in albums:
                albums[album.id] = album.songs.count()
            
            if albums[album.id]>1:
                song.delete()
                albums[album.id]-=1
            else :
                has_error = True

        if has_error:
              messages.add_message(request, messages.ERROR, 'you cant delete all songs of an album')    
        