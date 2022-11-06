from rest_framework.response import Response
from .serilaizer import AlbumSerializer,AlbumPostSerializer
from rest_framework import status
from .models import Album
from rest_framework.generics import ListAPIView
from knox.auth import TokenAuthentication
from musicplatform.permissions import IsAuthenticatedorReadOnly,IsTheUserArtistOrReadOnly


class AlbumView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticatedorReadOnly&IsTheUserArtistOrReadOnly]
    queryset = Album.objects.filter(is_approved=True)
    serializer_class = AlbumSerializer


    def post(self, request):
        serilaizer = AlbumPostSerializer(data={**request.data,"artist":request.user.artist.id})
        if serilaizer.is_valid():
            serilaizer.save()
            return Response ({"msg":"album created"},status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)

    


