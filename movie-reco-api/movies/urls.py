from django.urls import path
from .views import TrendingMoviesView, SearchMoviesView, UserFavouriteMoviesView, RemoveFavoriteView

app_name = 'movies'

urlpatterns = [
    path('trending/', TrendingMoviesView.as_view(), name='trending'),
    path('search/', SearchMoviesView.as_view(), name='search'),
    path('favorites/', UserFavouriteMoviesView.as_view(), name='favorites'),
    path('favorites/<int:pk>/', RemoveFavoriteView.as_view(), name='remove_favorite'),
]
