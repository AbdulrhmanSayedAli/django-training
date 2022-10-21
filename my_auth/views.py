from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout

class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"msg":"successfully logged in"})
        
        return Response({"msg":"invalid login"})

       
class LogOutView(APIView):
    def post(self,request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"msg":"successfully logged out"})
            
        return Response({"msg":"already logged out"})