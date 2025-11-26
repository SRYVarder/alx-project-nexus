import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestAuth:
    def test_register_user(self):
        client = APIClient()
        response = client.post('/api/auth/register/', {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'supersecret123'
         }, format='json')
        assert response.status_code == 201
        assert User.objects.filter(username='newuser').exists()

    def test_login_success(self):
        client = APIClient()
        User.objects.create_user(username='ken', password='pass123')
        response = client.post('/api/auth/login/', {
            'username': 'ken',
            'password': 'pass123'
        }, format='json')
        assert response.status_code == 200
        assert 'access' in response.json()
        assert 'refresh' in response.json()
        