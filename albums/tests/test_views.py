import pytest
import json
from artists.models import Artist
from albums.models import Album
from albums.serilaizer import AlbumSerializer
from users.models import User

@pytest.mark.django_db
def test_get_albums(api_client):
    user = User.objects.create_user(username="roctes",password="123456aa")
    artist1 = Artist.objects.create(stage_name="abdul",user=user)
    artist2 = Artist.objects.create(stage_name="abdul2",social_link="https://google.com")
    Album.objects.create(name="test",release_datetime="2022-2-2 12:12" ,cost=2,is_approved=True,artist=artist1)
    Album.objects.create(name="test22",release_datetime="2022-1-2 12:12" ,cost=122,is_approved=True,artist=artist1)
    Album.objects.create(release_datetime="2021-2-2 12:12" ,cost=12,artist=artist2)
    client = api_client()
    response = client.get('/albums/')
    assert response.status_code == 200
    response_content = json.loads(response.content.decode("unicode_escape"))
    serializer = AlbumSerializer(Album.objects.filter(is_approved=True),many=True)
    expected_response_content = serializer.data
    assert response_content["results"] == expected_response_content
    

@pytest.mark.django_db
def test_get_albums_with_filter(api_client):
    user = User.objects.create_user(username="roctes",password="123456aa")
    artist1 = Artist.objects.create(stage_name="abdul",user=user)
    artist2 = Artist.objects.create(stage_name="abdul2",social_link="https://google.com")
    Album.objects.create(name="test",release_datetime="2022-2-2 12:12" ,cost=2,is_approved=True,artist=artist1)
    Album.objects.create(name="test22",release_datetime="2022-1-2 12:12" ,cost=122,is_approved=True,artist=artist1)
    Album.objects.create(release_datetime="2021-2-2 12:12" ,cost=12,artist=artist2,is_approved=True)
    client = api_client()
    response = client.get('/albums/?cost__gte=10')
    assert response.status_code == 200
    response_content = json.loads(response.content.decode("unicode_escape"))
    serializer = AlbumSerializer(Album.objects.filter(is_approved=True,cost__gte=10),many=True)
    expected_response_content = serializer.data
    assert response_content["results"] == expected_response_content
    

@pytest.mark.django_db
def test_post_no_auth(api_client):
    client = api_client()
    response = client.post('/albums/', {"name":"koko","release_datetime":"2011-12-12 10:10","cost":3},format="json")
    assert response.status_code == 401
    response_content = json.loads(response.content.decode("unicode_escape"))
    expected_response_content = {"detail":"Authentication credentials were not provided."}
    assert response_content == expected_response_content
    


@pytest.mark.django_db
def test_post_user_not_artist(api_client):
    user = User.objects.create_user(username="roctes", password="123456aa")
    client = api_client(user)
    response = client.post('/albums/', {"name":"koko","release_datetime":"2011-12-12 10:10","cost":3},format="json")
    assert response.status_code == 403
    response_content = json.loads(response.content.decode("unicode_escape"))
    expected_response_content = {"detail":"you must be an artist to do this request"}
    assert response_content == expected_response_content


@pytest.mark.django_db
def test_post(api_client):
    user = User.objects.create_user(username="roctes", password="123456aa")
    Artist.objects.create(stage_name="dd",user=user)
    client = api_client(user)
    response = client.post('/albums/', {"name":"koko2","release_datetime":"2011-12-12 10:10","cost":3},format="json")
    assert response.status_code == 201
    response_content = json.loads(response.content.decode("unicode_escape"))
    expected_response_content = {"msg":"album created"}
    assert response_content == expected_response_content
    
    