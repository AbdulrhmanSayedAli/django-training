import pytest
from rest_framework.test import APIClient
from knox.models import AuthToken

@pytest.fixture
def api_client():
    def result_func(user=None):
        client = APIClient()
        if  user :            
            instance, token = AuthToken.objects.create(user)
            client.force_authenticate(user=user,token=instance)
            
        return client
    return result_func