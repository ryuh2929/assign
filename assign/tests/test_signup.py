import pytest
from rest_framework import status
from django.urls import reverse

@pytest.mark.django_db
def test_signup(client):
    url = reverse('signup')
    data = {
        "username": "JIN HO",
        "password": "12341234",
        "password2": "12341234",
        "nickname": "Mentos"
    }
    
    response = client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        "username": "JIN HO",
        "nickname": "Mentos",
        "roles": [{"role": "USER"}]
    }
