from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .caching import get_cached_trending
from .external_api import search_movie
from .serializers import MovieSerializer, FavoriteMovieSerializer
from .models import FavoriteMovie

class TrendingMoviesView(APIView):
    def get(self, request):
        page = int(request.query_params.get('page', 1))
        data = get_cached_trending(page)
        return Response(data)
    
class SearchMoviesView(APIView):
    def get(self, request):
        query = request.query_params.get('query', '')
        if not query:
            return Response({"error": "Query parameter is required.", "example": "/api/movies/search/?query=the godfather"}, status=400)
        data = search_movie(query)
        return Response(data)
    
class UserFavouriteMoviesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        favourites = FavouriteMovie.objects.filter(user=request.user)
        serializer = FavouriteMovieSerializer(favourites, many=True)
        return Response(serializer.data)

    def post(self, request):
        tmdb_id = request.data.get('tmdb_id')
        title = request.data.get('title')
        poster = request.data.get('poster_path')

        favorite, created = FavouriteMovie.objects.get_or_create(
            user=request.user,
            tmdb_id=tmdb_id,
            defaults={'title': title, 'poster_path': poster}
        )
        if not created:
            return Response({"message": "Movie already in favourites."}, status=400)
        return Response(FavouriteMovieSerializer(favorite).data, status=201)
    
class RemoveFavoriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
            try:
                favorite = FavouriteMovie.objects.get(tmdb_id=pk, user=request.user)
                favorite.delete()
                return Response(status=204)
            except FavouriteMovie.DoesNotExist:
                return Response({"error": "Favourite movie not found."}, status=404)