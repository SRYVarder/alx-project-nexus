import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
class TestMovieEndpoints:
    def test_trending_unauthenticated(self):
        client = APIClient()
        response = client.get(reverse('movies:trending'))
        assert response.status_code == 200
        assert 'results' in response.json()

    def test_add_favorite_requires_auth(self):
        client = APIClient()
        url = reverse('movies:favorites')
        data = {'tmdb_id': 550, 'title': 'Fight Club'}
        response = client.post(url, data, format='json')
        assert response.status_code == 401
        