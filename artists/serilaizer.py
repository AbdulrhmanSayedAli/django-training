from rest_framework import serializers
from .models import Artist
from albums.models import Album


class InnerAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id","name","created","release_datetime","cost"]

class ArtistSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField()
    social_link = serializers.URLField(required=False)
    albums = InnerAlbumSerializer(many=True,required=False)

    class Meta:
        model = Artist
        fields = "__all__"