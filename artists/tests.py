from django.test import TestCase,RequestFactory
from .models import Artist  
from .views import ArtistsView
from .serilaizer import  ArtistSerializer

class ArtistTests(TestCase):
    def setUp(self):
        Artist.objects.create(stage_name="abdul",social_link="http:...")
        Artist.objects.create(stage_name="ahmed")

    def test_insert(self):  
        artist1 = ArtistSerializer(Artist.objects.get(id=1))
        artist2 = ArtistSerializer(Artist.objects.get(id=2))
        self.assertEqual(artist1.data,{"id":1,"stage_name":"abdul","social_link":"http:...","albums":[]}) 
        self.assertEqual(artist2.data,{"id":2,"stage_name":"ahmed","social_link":"","albums":[]})

    def test_get_all(self):
         request = RequestFactory().get('/artists/')
         response = ArtistsView.as_view()(request)
         all_artists = ArtistSerializer(Artist.objects.all().prefetch_related("albums"),many=True)
         self.assertEqual(all_artists.data,response.data)
