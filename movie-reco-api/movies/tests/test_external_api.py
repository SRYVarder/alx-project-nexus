from unittest.mock import patch
import requests_mock
from movies.external_api import get_trending_movies

def test_get_trending_movies():
    mock_response = {
        "page": 1,
        "results": [
            {"id": 550, "title": "Fight Club"}]
    }
    with requests_mock.Mocker() as m:
        m.get("https://api.themoviedb.org/3/trending/movie/week", json=mock_response)
        data = get_trending_movies()
        assert data['results'][0]['title'] == "Fight Club"
        assert len(data["results"]) == 1   
        