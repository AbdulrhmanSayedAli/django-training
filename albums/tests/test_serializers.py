from albums.serilaizer import AlbumSerializer , AlbumPostSerializer
from artists.models import Artist
from albums.models import Album
from users.models import User
import pytest



def Artist_To_Json(artist):
    result =  {
        "id":artist.id,
        "stage_name":artist.stage_name,
        "social_link":artist.social_link,
        "user":None,
    }
    if artist.user:
        result["user"] = artist.user.id
    return result

def Album_To_Json(album):
    return {
        "id":album.id,
        "name":album.name,
        "release_datetime":album.release_datetime,
        "cost":float(album.cost),
        "is_approved":album.is_approved,
        "artist":Artist_To_Json(album.artist),
    }



@pytest.mark.django_db
def test_serialize():
    user = User.objects.create(username="dd",password="12345aa")
    artist = Artist.objects.create(stage_name="roctes",user=user)
    album = Album.objects.create(name="koko",artist=artist,release_datetime="2022-11-11 12:12",cost=22)
    serializer = AlbumSerializer(album)
    expected_json_data = Album_To_Json(album)
    print(expected_json_data)
    print(serializer.data)
    assert expected_json_data["id"] == serializer.data["id"]
    assert expected_json_data["name"] == serializer.data["name"]
    assert expected_json_data["release_datetime"] == serializer.data["release_datetime"]
    assert expected_json_data["cost"]== float(serializer.data["cost"])
    assert expected_json_data["is_approved"] == serializer.data["is_approved"]
    assert expected_json_data["artist"] == serializer.data["artist"]



@pytest.mark.django_db
def test_deserialize():
    user = User.objects.create(username="dd",password="12345aa")
    artist = Artist.objects.create(stage_name="roctes",user=user)
    raw_json = {
        "name":"koko",
        "release_datetime":"2011-12-12 10:10:00+00:00",
        "cost":3,
        "artist":artist.id,
        "is_approved":True
    }
    serializer = AlbumPostSerializer(data=raw_json)
    assert serializer.is_valid()
    serializer.save()
    created_album = Album.objects.filter(name="koko").first()
    assert created_album.name == raw_json["name"]
    assert str(created_album.release_datetime) == raw_json["release_datetime"]
    assert created_album.cost == raw_json["cost"]
    assert created_album.artist.id == raw_json["artist"]
    assert created_album.is_approved == raw_json["is_approved"]
    