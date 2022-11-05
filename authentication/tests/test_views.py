from users.models import User
from knox.models import AuthToken
import pytest
import json


@pytest.mark.django_db
def test_register_missing_email(api_client):
    client = api_client()
    response =  client.post('/authentication/register', {"username":"dd2","password1":"aaa12345","password2":"aaa12345"}, format='json')
    assert response.status_code == 400
    expected_response_content = {"email": ["This field is required."]}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 

@pytest.mark.django_db
def test_register_missing_all_data(api_client):
    client = api_client()
    response =  client.post('/authentication/register', {}, format='json')
    assert response.status_code == 400
    expected_response_content = {"email":["This field is required."],"username":["This field is required."],"password1":["This field is required."],"password2":["This field is required."]}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 


@pytest.mark.django_db
def test_register_password_dont_match(api_client):
    client = api_client()
    response =  client.post('/authentication/register', {"username":"dd2","password1":"aaa12345","password2":"12345","email":"dd@gmail.com"}, format='json')
    assert response.status_code == 400
    expected_response_content = {"non_field_errors":["Those passwords don't match."]}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 


@pytest.mark.django_db
def test_register_weak_password(api_client):
    client = api_client()
    response =  client.post('/authentication/register', {"username":"dd2","password1":"2345","password2":"2345","email":"dd@gmail.com"}, format='json')
    assert response.status_code == 400
    expected_response_content = {"non_field_errors":["This password is too short. It must contain at least 8 characters.","This password is too common.","This password is entirely numeric."]}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content


@pytest.mark.django_db
def test_register_username_in_use(api_client):
    User.objects.create_user(username="dd2",password="123456aa")
    client = api_client()
    response = client.post('/authentication/register', {"username":"dd2","password1":"aaa12345","password2":"aaa12345","email":"dd@gmail.com"}, format='json')
    assert response.status_code == 400
    expected_response_content = {"username":["Your username is already in use"]}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 


@pytest.mark.django_db
def test_register_already_logged_in(api_client):
    user = User.objects.create_user(username="dd2", password="aaa12345")
    client = api_client(user)
    response = client.post('/authentication/register', {"username":"dd2","password1":"aaa12345","password2":"aaa12345","email":"dd@gmail.com"}, format='json')
    assert response.status_code == 403
    expected_response_content = {"detail":"You do not have permission to perform this action."}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 



@pytest.mark.django_db
def test_register(api_client):
    client = api_client()
    response = client.post('/authentication/register', {"username":"dd2","password1":"aaa12345","password2":"aaa12345","email":"dd@gmail.com"}, format='json')
    assert response.status_code == 200
    expected_response_content = {"result":"user created successfully"}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 



@pytest.mark.django_db
def test_login (api_client):
    client = api_client()
    user = User.objects.create_user(username="roctes7", password="123456aa")
    response = client.post('/authentication/login', {"username":"roctes7","password":"123456aa"}, format='json')
    assert response.status_code == 200

    expected_response_content_user = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "bio": user.bio
    }
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content["user"] == expected_response_content_user 


@pytest.mark.django_db
def test_login_already_logged_in (api_client):
    user = User.objects.create_user(username="roctes7", password="123456aa")
    client= api_client(user)
    response = client.post('/authentication/login', {"username":"roctes7","password":"123456aa"}, format='json')
    assert response.status_code == 403
    expected_response_content = {"detail":"You do not have permission to perform this action."}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 



@pytest.mark.django_db
def test_logout (api_client):
    user = User.objects.create_user(username="ddd",password="123456aa")
    client = api_client(user)
    response = client.post('/authentication/logout',{},format="json")
    assert response.status_code == 200
    expected_response_content = {"result":"successfully logged out"}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 


@pytest.mark.django_db
def test_logout_already_logged_out (api_client):
    client = api_client()
    response = client.post('/authentication/logout', {}, format='json')
    assert response.status_code == 401
    expected_response_content = {"detail":"Authentication credentials were not provided."}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 