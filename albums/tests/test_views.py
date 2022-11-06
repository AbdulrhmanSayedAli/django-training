# import pytest
# import json
# from artists.models import Artist
# from albums.models import Album
# from albums.serilaizer import AlbumSerializer

# @pytest.mark.django_db
# def test_post_missing_all_data(api_client):
#     client = api_client()
#     response = client.post('/albums/', {}, format='json')
#     assert response.status_code == 400
#     expected_response_content = {"release_datetime":["This field is required."],"cost":["This field is required."],"artist":["This field is required."]}
#     response_content = json.loads(response.content.decode("unicode_escape"))
#     assert response_content == expected_response_content 


# @pytest.mark.django_db
# def test_post_missing_artist(api_client):
#     client = api_client()
#     response = client.post('/albums/', {"name":"ss","release_datetime":"2022-1-1 12:12","cost":33}, format='json')
#     assert response.status_code == 400
#     expected_response_content = {"artist":["This field is required."]}
#     response_content = json.loads(response.content.decode("unicode_escape"))
#     assert response_content == expected_response_content 


# @pytest.mark.django_db
# def test_post_artist_not_found(api_client):
#     client = api_client()
#     response = client.post('/albums/', {"name":"ss","release_datetime":"2022-1-1 12:12","cost":33,"artist":33}, format='json')
#     assert response.status_code == 400

# @pytest.mark.django_db
# def test_post(api_client):
#     client = api_client()
#     artist = Artist.objects.create(stage_name="mah")
#     response = client.post('/albums/', {"name":"ss","release_datetime":"2022-1-1 12:12","cost":33,"artist":artist.id}, format='json')
#     assert response.status_code == 201
#     expected_response_content = {"msg":"album created"}
#     response_content = json.loads(response.content.decode("unicode_escape"))
#     assert response_content == expected_response_content 


# @pytest.mark.django_db
# def test_get(api_client):
#     client = api_client()
#     artist1 = Artist.objects.create(stage_name="mah")
#     artist2 = Artist.objects.create(stage_name="mah2")
#     Album.objects.create(name="dd",release_datetime="2022-1-1 12:12",cost=22,artist=artist1)
#     Album.objects.create(name="d2d",release_datetime="2012-1-1 12:12",cost=232,artist=artist2)
#     Album.objects.create(release_datetime="2012-1-1 12:12",cost=2032,artist=artist2)
#     response = client.get('/albums/', {}, format='json')
#     assert response.status_code == 200
#     serilizer = AlbumSerializer(Album.objects.all(),many=True)
#     expected_response_content = serilizer.data
#     response_content = json.loads(response.content.decode("unicode_escape"))
#     assert response_content == expected_response_content 
