from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework import status
from .serializers import UserSerializer
from musicplatform.permissions import IsSameUserOrReadOnly
from knox.auth import TokenAuthentication
from musicplatform.permissions import IsAuthenticatedorReadOnly

class UserView (APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticatedorReadOnly&IsSameUserOrReadOnly]
    
    def get (self,request,pk):
        user = User.objects.filter(pk=pk)
        if not user :
            return Response({"result":"no such user found"},status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user[0])
        return Response(serializer.data)


    def CustomUpdate(self,request,pk,partial):
        user = User.objects.filter(pk=pk)
        if not user :
            return Response({"result":"no such user found"},status=status.HTTP_404_NOT_FOUND)
        user = user[0]
        serializer = UserSerializer(user,data=request.data,partial=partial)
        if not serializer.is_valid():
             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        self.check_object_permissions(self.request, user)
        serializer.update(user,serializer.validated_data)
        return Response(serializer.data)

    def put (self,request,pk):
        return self.CustomUpdate(request,pk,False)

    def patch (self,request,pk):
        return self.CustomUpdate(request,pk,True)

    