from rest_framework import serializers
from .models import Artist
from albums.models import Album


class ArtistSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField()
    social_link = serializers.URLField(required=False)

    class Meta:
        model = Artist
        fields = "__all__"


class InnerAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id","name","created","release_datetime","cost"]

class ALLArtistsSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField()
    social_link = serializers.URLField(required=False)
    albums = InnerAlbumSerializer(many=True)

    class Meta:
        model = Artist
        fields = ["id","stage_name","social_link","albums"]
