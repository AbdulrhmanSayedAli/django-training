from django.contrib import admin
from .models import Artist
# Register your models here.



@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("stage_name", "social_link", "approved_albums")

    fieldsets = (
        (None, {
            'fields': ('stage_name',"social_link","albums")
        }),

    )

    


