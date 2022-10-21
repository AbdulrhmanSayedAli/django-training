from django.test import TestCase,RequestFactory
from .models import Album
from .serilaizer import AlbumSerializer
from artists.models import Artist
from .views import AlbumView

class ArtistTests(TestCase):
    def setUp(self):
        artist1 = Artist.objects.create(stage_name="abdul",social_link="http:...")
        artist2 = Artist.objects.create(stage_name="ahmed")
        Album.objects.create(name="qora",artist=artist1,release_datetime="2022-11-11 10:10",cost=11)
        Album.objects.create(name="aaa",artist=artist2,release_datetime="2022-11-11 10:10",cost=12,is_approved=True)
        Album.objects.create(artist=artist2,release_datetime="2022-11-11 10:10",cost=111)


    def test_get_albums(self):
        all_albums = AlbumSerializer(Album.objects.all(),many=True)
        request = RequestFactory().get('/albums/')
        response = AlbumView.as_view()(request)
        self.assertEqual(response.data,all_albums.data)