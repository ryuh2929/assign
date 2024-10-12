import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_login():
    # APIClient 초기화
    client = APIClient()
    
    # 테스트 유저 생성
    user_data = {
        'username': 'JIN HO',
        'password': '12341234',
        'password2': '12341234',
        'nickname': 'Mentos',
    }
    
    # 유저를 실제로 생성 (가입 과정 필요)
    response = client.post(reverse('signup'), user_data)
    assert response.status_code == status.HTTP_201_CREATED

    login_data = {
        'username': 'JIN HO',
        'password': '12341234',
    }
    
    response = client.post(reverse('login'), login_data)
    
    assert response.status_code == status.HTTP_200_OK
    assert 'refresh' in response.data 
    assert 'access' in response.data  

    refresh_token = response.data['refresh']
    access_token = response.data['access']
    
    # JWT 토큰 형식 확인 (헤더, 페이로드, 서명으로 구성된 3부분)
    assert len(refresh_token.split('.')) == 3
    assert len(access_token.split('.')) == 3

