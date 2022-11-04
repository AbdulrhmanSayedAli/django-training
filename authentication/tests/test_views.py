from users.models import User
import pytest


@pytest.mark.django_db
def test_register(api_client):
    client = api_client()
    response =  client.post('/authentication/register', {"username":"dd2","password1":"aaa12345","password2":"aaa12345"}, format='json')
    assert response.status_code == 400

    response =  client.post('/authentication/register', {}, format='json')
    assert response.status_code == 400

    response =  client.post('/authentication/register', {"username":"dd2","password1":"aaa12345","password2":"12345","email":"dd@gmail.com"}, format='json')
    assert response.status_code == 400

    response =  client.post('/authentication/register', {"username":"dd2","password1":"2345","password2":"2345","email":"dd@gmail.com"}, format='json')
    assert response.status_code == 400

    response = client.post('/authentication/register', {"username":"dd2","password1":"aaa12345","password2":"aaa12345","email":"dd@gmail.com"}, format='json')
    assert response.status_code == 200

    #user name already in use
    response = client.post('/authentication/register', {"username":"dd2","password1":"aaa12345","password2":"aaa12345","email":"dd@gmail.com"}, format='json')
    assert response.status_code == 400

    client = api_client({"username":"dd2","password":"aaa12345"})

    #already logged in
    response = client.post('/authentication/register', {"username":"dd2","password1":"aaa12345","password2":"aaa12345","email":"dd@gmail.com"}, format='json')
    assert response.status_code == 403

@pytest.mark.django_db
def test_login (api_client):
    client = api_client()
    User.objects.create_user(username="roctes7", password="123456aa")
    response = client.post('/authentication/login', {"username":"roctes7","password":"123456aa"}, format='json')
    assert response.status_code == 200

    #already logged in
    response = client.post('/authentication/login', {"username":"roctes7","password":"123456aa"}, format='json')
    assert response.status_code == 403



@pytest.mark.django_db
def test_logout (api_client):
    client = api_client()
    user_Data = {"username":"dataa", "password":"123456aa"}

    #already logged out
    response = client.post('/authentication/logout', {}, format='json')
    assert response.status_code == 401

    User.objects.create_user(**user_Data)
    client = api_client(user_Data)

    response = client.post('/authentication/logout',json={})
    assert response.status_code == 200