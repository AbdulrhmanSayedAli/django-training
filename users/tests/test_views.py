import pytest
import json
from users.models import User


@pytest.mark.django_db
def test_get_user_not_found(api_client):
    client = api_client()
    response = client.get("/users/23")
    assert response.status_code == 404
    expected_response_content = {"result":"no such user found"}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 


@pytest.mark.django_db
def test_get_user(api_client): 
    User.objects.create_user(username="roctessss",password="12345678aa",email="test@gmail.com",bio="my bio")
    client = api_client()
    response = client.get("/users/1")
    assert response.status_code == 200
    expected_response_content = {"id":1,"username":"roctessss","email":"test@gmail.com","bio":"my bio"}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content

@pytest.mark.django_db
def test_put_not_authenticated(api_client): 
    user = User.objects.create_user(username="roctessss",password="12345678aa",email="test@gmail.com",bio="my bio")
    client = api_client()
    response =  client.put('/users/'+str(user.id), {"username":"dd2","email":"aa@gmail.com","bio":"hellosdsd"}, format='json')
    assert response.status_code == 401
    expected_response_content = {"detail":"Authentication credentials were not provided."}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 

@pytest.mark.django_db
def test_put_not_same_user(api_client):
    user1 = User.objects.create_user(username="roctessss",password="12345678aa",email="test@gmail.com",bio="my bio")
    user2 = User.objects.create_user(username="roctessss2",password="12345678aa",email="test2@gmail.com",bio="my bio2")
    client = api_client(user1)
    response =  client.put('/users/'+str(user2.id), {"username":"dd2","email":"aa@gmail.com","bio":"hellosdsd"}, format='json')
    assert response.status_code == 403
    expected_response_content = {'detail': 'You do not have permission to perform this action.'}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 

@pytest.mark.django_db
def test_put_missing_data(api_client):
    user = User.objects.create_user(username="roctessss",password="12345678aa",email="test@gmail.com",bio="my bio")
    client = api_client(user)
    response =  client.put('/users/'+str(user.id), {"username":"dd2"}, format='json')
    assert response.status_code == 400
    expected_response_content = {"email":["This field is required."],"bio":["This field is required."]}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content


@pytest.mark.django_db
def test_put(api_client):
    user = User.objects.create_user(username="roctessss",password="12345678aa",email="test@gmail.com",bio="my bio")
    client = api_client(user)
    response =  client.put('/users/'+str(user.id), {"username":"dd2asdasd","email":"aa@gmail.com","bio":"hellosdsd"}, format='json')
    assert response.status_code == 200
    expected_response_content = {"id":user.id,"username":"dd2asdasd","email":"aa@gmail.com","bio":"hellosdsd"}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content


@pytest.mark.django_db
def test_patch_not_authenticated(api_client): 
    user = User.objects.create_user(username="roctessss",password="12345678aa",email="test@gmail.com",bio="my bio")
    client = api_client()
    response =  client.patch('/users/'+str(user.id), {"username":"dd2","email":"aa@gmail.com","bio":"hellosdsd"}, format='json')
    assert response.status_code == 401
    expected_response_content = {"detail":"Authentication credentials were not provided."}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 


@pytest.mark.django_db
def test_patch_not_same_user(api_client):
    user1 = User.objects.create_user(username="roctessss",password="12345678aa",email="test@gmail.com",bio="my bio")
    user2 = User.objects.create_user(username="roctessss2",password="12345678aa",email="test2@gmail.com",bio="my bio2")
    client = api_client(user1)
    response =  client.patch('/users/'+str(user2.id), {"username":"dd2","email":"aa@gmail.com","bio":"hellosdsd"}, format='json')
    assert response.status_code == 403
    expected_response_content = {'detail': 'You do not have permission to perform this action.'}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content 



@pytest.mark.django_db
def test_patch_wrong_email(api_client):
    user = User.objects.create_user(username="roctessss",password="12345678aa",email="test@gmail.com",bio="my bio")
    client = api_client(user)
    response =  client.patch('/users/'+str(user.id), {"email":"dd2"}, format='json')
    assert response.status_code == 400
    expected_response_content = {"email":["Enter a valid email address."]}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content


@pytest.mark.django_db
def test_patch(api_client):
    user = User.objects.create_user(username="roctessss",password="12345678aa",email="test@gmail.com",bio="my bio")
    client = api_client(user)
    response =  client.patch('/users/'+str(user.id), {"email":"dd2@gmail.com"}, format='json')
    assert response.status_code == 200
    expected_response_content = {"id":user.id,"username":"roctessss","email":"dd2@gmail.com","bio":"my bio"}
    response_content = json.loads(response.content.decode("unicode_escape"))
    assert response_content == expected_response_content