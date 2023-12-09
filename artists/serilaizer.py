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
    

    def validate_stage_name(self, value):
        if Artist.objects.filter(stage_name=value).exists():
            raise serializers.ValidationError("stage name is not unique")
        return value


    class Meta:
        model = Artist
        fields = "__all__"