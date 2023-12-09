from rest_framework.response import Response
from .serilaizer import AlbumSerializer,AlbumPostSerializer
from rest_framework import status
from .models import Album
from rest_framework.generics import ListAPIView
from knox.auth import TokenAuthentication
from musicplatform.permissions import IsAuthenticatedorReadOnly,IsTheUserArtistOrReadOnly
from django_filters import rest_framework as filters
from .filters import AlbumFilter

class AlbumView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticatedorReadOnly&IsTheUserArtistOrReadOnly]
    queryset = Album.objects.filter(is_approved=True)
    serializer_class = AlbumSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('cost', 'name')
    filterset_class = AlbumFilter


    def post(self, request):
        serilaizer = AlbumPostSerializer(data={**request.data,"artist":request.user.artist.id})
        if serilaizer.is_valid():
            serilaizer.save()
            return Response ({"msg":"album created"},status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)



class ManualAlbumView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticatedorReadOnly&IsTheUserArtistOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


    def isValidCost(self,value):
        try:
            float(value)
        except :
            return False
        return float(value)>=0

    def get(self, request):
        query_params = request.query_params
        cost__lte = query_params.get('cost__lte') or 999999999999
        cost__gte = query_params.get('cost__gte') or 0
        name = query_params.get('name') or ""
        errors = []

        if not self.isValidCost(cost__lte):
            errors.append("cost__lte must be a positive number")

        if not self.isValidCost(cost__gte):
            errors.append("cost__gte must be a positive number")
        
        if errors:
            return Response({"errors":errors},status=status.HTTP_400_BAD_REQUEST)

        cost__lte = float (cost__lte)
        cost__gte = float (cost__gte)

        print(name)
        self.queryset = self.queryset.filter(cost__gte=cost__gte,cost__lte=cost__lte,name__icontains=name)
        return self.list(request)
    


