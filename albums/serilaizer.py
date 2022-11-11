from rest_framework import serializers
from .models import Album
from .models_validators import costValidator
from artists.models import Artist 

class InnerArtistSerilizer(serializers.ModelSerializer):
    stage_name = serializers.CharField()
    social_link = serializers.URLField(required=False)
    
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="New Album")
    release_datetime  = serializers.DateTimeField()
    cost = serializers.DecimalField(validators=[costValidator],decimal_places=5,max_digits=10)
    is_approved = serializers.BooleanField(default=False)
    artist = InnerArtistSerilizer()

    class Meta:
        model = Album
        fields = '__all__'


class AlbumPostSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="New Album")
    release_datetime  = serializers.DateTimeField()
    cost = serializers.DecimalField(validators=[costValidator],decimal_places=5,max_digits=10)
    is_approved = serializers.BooleanField(default=False)


    class Meta:
        model = Album
        fields = '__all__'
