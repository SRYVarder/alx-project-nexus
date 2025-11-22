from celery import shared_task
from django.core.cache import cache
from .external_api import get_trending_movies
import logging

logger = logging.getLogger(__name__)

@shared_task
def update_trending_cache():
    """
    Celery task to update the cached trending movies.
    Fetches the latest trending movies from the external API and updates the cache.
    """
    logger.info("Updating trending movies cache...")
    for page in range(1, 6):  # Update first 5 pages
        data = get_trending_movies(page)
        cache_key = f"trending_page_{page}"
        cache.set(cache_key, data, timeout=3600*3)  # Cache for 3 hours 
    logger.info("Trending cache updated successfully")