from django.urls import path
from .views import TrendingMoviesView, SearchMoviesView, UserFavouriteMoviesView, RemoveFavoriteView

urlpatterns = [
    path('trending/', TrendingMoviesView.as_view(), name='trending-movies'),
    path('search/', SearchMoviesView.as_view(), name='search-movies'),
    path('favorites/', UserFavouriteMoviesView.as_view(), name='user-favorites'),
    path('favorites/<int:pk>/', RemoveFavoriteView.as_view(), name='remove-favorite'),
]
