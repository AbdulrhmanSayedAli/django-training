from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField()
    social_link = serializers.URLField(required=False)

    class Meta:
        model = Artist
        fields = '__all__'
