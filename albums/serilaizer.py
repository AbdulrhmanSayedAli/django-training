from rest_framework import serializers
from .models import Album
from .models_validators import costValidator
class AlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="New Album")
    release_datetime  = serializers.DateTimeField()
    cost = serializers.DecimalField(validators=[costValidator],decimal_places=5,max_digits=10)
    is_approved = serializers.BooleanField(default=False)

    class Meta:
        model = Album
        fields = '__all__'
