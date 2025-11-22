from django.core.cache import cache
from .external_api import get_trending_movies
import logging

logger = logging.getLogger(__name__)

def get_cached_trending(page=1):
    """
    Retrieves trending movies from cache or fetches from external API if not cached.
    Caches the result for future requests.
    """
    cache_key = f"trending_page_{page}"
    data = cache.get(cache_key)
    
    if not data:
        logger.info(f"Cache miss - fetching trending from TMDb")
        data = get_trending_movies(page)
        cache.set(cache_key, data, timeout=3600*2)  # Cache for 2 hour
    else:
        logger.info(f"Cache hit for {cache_key}.")
    
    return data

def get_cached_recommendations(movie_id, page=1):
    """
    Retrieves movie recommendations from cache or fetches from external API if not cached.
    Caches the result for future requests.
    """
    cache_key = f"recommendations_{movie_id}"
    data = cache.get(cache_key)
    
    if not data:
        from .external_api import get_recommendations
        data = get_recommendations(movie_id)
        cache.set(cache_key, data, timeout=3600*24)  # Cache for 24 hours
    return data
