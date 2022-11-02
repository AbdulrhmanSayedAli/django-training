from msilib.schema import SelfReg
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilaizer import ArtistSerializer
from rest_framework import status
from .models import Artist

class ArtistsView(APIView):
    def post(self, request):
        serilaizer = ArtistSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response ({"msg":"artist created"},status=status.HTTP_201_CREATED)
            
        return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get (self,request):
        queryset = Artist.objects.all()
        queryset = queryset.prefetch_related('albums')
        serializer = ArtistSerializer(queryset.all(),many=True)
        print(request.user.is_authenticated)
        return Response(serializer.data)