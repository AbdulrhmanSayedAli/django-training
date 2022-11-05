from rest_framework.views import APIView
from rest_framework.response import Response
from musicplatform.permissions import IsAuthenticatedorReadOnly,IsSuperUser
from .serializers import RegisterUserSerializer
from users.serializers import UserSerializer
from users.models import User
from django.contrib.auth import authenticate, login ,logout
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogOutView
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_framework import status

class Register (APIView):
    permission_classes=[~IsAuthenticatedorReadOnly|IsSuperUser]
    def post (self,request):
        serializer = RegisterUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        User.objects.create_user(username=serializer.data["username"],
                                 email=serializer.data["email"],
                                 password=serializer.data["password1"])
        return Response({"result":"user created successfully"},status=status.HTTP_201_CREATED)


class Login (KnoxLoginView):
    permission_classes=[~IsAuthenticatedorReadOnly]
    def post (self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            instance, token = AuthToken.objects.create(user)
            return Response({"token":token,"user":serializer.data})
        
        return Response({"result":"invalid login"},status=status.HTTP_400_BAD_REQUEST)


class LogOut (KnoxLogOutView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticatedorReadOnly]
    def post (self,request,*args,**kwargs):
        logout(request)
        super().post(request,*args,**kwargs)
        return Response({"result":"successfully logged out"})
