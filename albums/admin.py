from django.contrib import admin
from .models import Album
# Register your models here.


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')
    list_display = ("name", "is_approved")