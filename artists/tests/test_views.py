import pytest
import json
from artists.serilaizer import ArtistSerializer
from artists.models import Artist

@pytest.mark.django_db
def test_post_artist_missing_stage_name(api_client):
    client = api_client()
    response =  client.post('/artists/', {}, format='json')
    assert response.status_code == 400
    expected_response_content = {"stage_name":["This field is required."]}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content


@pytest.mark.django_db
def test_post_unvalid_url(api_client):
    client = api_client()
    response =  client.post('/artists/', {"stage_name":"mj","social_link":"sdsd"}, format='json')
    assert response.status_code == 400
    expected_response_content = {"social_link":["Enter a valid URL."]}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content



@pytest.mark.django_db
def test_post_artist(api_client):
    client = api_client()
    response =  client.post('/artists/', {"stage_name":"mj","social_link":"https://sdsd.com"}, format='json')
    assert response.status_code == 201
    expected_response_content = {"msg":"artist created"}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content


@pytest.mark.django_db
def test_get_all_artists(api_client):
    Artist.objects.create(stage_name="test")
    Artist.objects.create(stage_name="test2",social_link="https://google.com")
    client = api_client()
    response =  client.get('/artists/')
    assert response.status_code == 200
    queryset = Artist.objects.all()
    queryset = queryset.prefetch_related('albums')
    serializer = ArtistSerializer(queryset.all(),many=True)
    expected_response_content = serializer.data
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content
