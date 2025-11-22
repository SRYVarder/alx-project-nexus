import requests
from django.conf import settings
from requests.exceptions import RequestException
import logging

logger = logging.getLogger(__name__)

def get_trending_movies(page=1):
    """
    Fetches trending movies from the external movie database API.
    Returns a list of trending movies or raises an exception on failure.
    """
    try:
        url = f"{settings.TMDB_BASE_URL}/trending/movie/week"
        params = {
            'api_key': settings.TMDB_API_KEY,
            'page': page
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logger.error(f"Error fetching trending movies: {e}")
        return {"results": []}
    
def get_recommendations(movie_id, page=1):

    """
    Fetches movie recommendations based on a given movie ID from the external movie database API.
    Returns a list of recommended movies or raises an exception on failure.
    """
    try:
        url = f"{settings.TMDB_BASE_URL}/movie/{movie_id}/recommendations"
        params = {
            'api_key': settings.TMDB_API_KEY,
            'page': page
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logger.error(f"Error fetching recommendations for {movie_id}: {e}")
        return {"results": []}
    
def search_movie(query, page=1):
    """
    Searches for movies based on a query string from the external movie database API.
    Returns a list of movies matching the search query or raises an exception on failure.
    """
    try:
        url = f"{settings.TMDB_BASE_URL}/search/movie"
        params = {
            'api_key': settings.TMDB_API_KEY,
            'query': query,
            'page': page
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logger.error(f"Error searching movies with query '{query}': {e}")
        return {"results": []}
    