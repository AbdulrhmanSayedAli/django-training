import pytest
from rest_framework.test import APIClient
from knox.models import AuthToken
from users.models import User

@pytest.fixture
def api_client():
    def result_func(user=None):
        client = APIClient()
        if  user :
            client.post('/authentication/login', {"username":user["username"],"password":user["password"]}, format='json')
            token = AuthToken.objects.get(user__username=user["username"])
            client.force_authenticate(user=User.objects.get(username=user["username"]),token=token)
        return client
    return result_func