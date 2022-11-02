from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAuthenticated,IsSuperUser
from .serializers import UserSerializer
from users.models import User

class Register (APIView):
    permission_classes=[~IsAuthenticated|IsSuperUser]
    def post (self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        User.objects.create_user(username=serializer.data["username"],
                                 email=serializer.data["email"],
                                 password=serializer.data["password1"])
        return Response("user created successfully")
