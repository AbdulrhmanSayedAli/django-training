from rest_framework.views import APIView
from rest_framework.response import Response

class ArtistsView(APIView):
    def post(self, request):
        return Response ({"msg":"end point created"})
