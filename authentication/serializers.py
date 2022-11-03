from rest_framework import serializers
from users.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate_username(self, username):
        existing = User.objects.filter(username=username).first()
        if existing:
            raise serializers.ValidationError("Your username is already in use")
        return username

    def validate(self, data):
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")

        password = data.get('password1')
        myData = dict(data)
        del myData["password1"]
        del myData["password2"]
        user = User(**myData,password=password)
        validate_password(password=password, user=user)

        return data
