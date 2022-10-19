from rest_framework.views import APIView
from rest_framework.response import Response
from .serilaizer import AlbumSerializer
from rest_framework import status

class AlbumView(APIView):
    def post(self, request):
        serilaizer = AlbumSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response ({"msg":"end point created"},status=status.HTTP_201_CREATED)
            
        return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)