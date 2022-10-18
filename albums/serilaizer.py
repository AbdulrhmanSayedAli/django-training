from rest_framework import serializers
from .models import Album
from django.core.exceptions import ValidationError

def costValidator(cost):
    if cost<0:
        raise ValidationError("Cost must be greater than or equal to zero")
    return cost

class AlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="New Album")
    release_datetime  = serializers.DateTimeField()
    cost = serializers.DecimalField(validators=[costValidator],decimal_places=5,max_digits=10)
    is_approved = serializers.BooleanField(default=False)

    class Meta:
        model = Album
        fields = '__all__'
