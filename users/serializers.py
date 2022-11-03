from rest_framework import serializers
from .models import User

class UserSerializer (serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    bio = serializers.CharField(max_length=256)

    def validate_username(self, username):
        existing = User.objects.filter(username=username).first()
        if existing:
            raise serializers.ValidationError("Your username is already in use")
        return username

    class Meta:
        model = User
        fields=("id","username","email","bio")