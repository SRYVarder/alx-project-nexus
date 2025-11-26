import pytest   
from django.contrib.auth import get_user_model
from movies.models import FavoriteMovie

User = get_user_model()

@pytest.mark.django_db
def test_favorite_movie_creation():
    user = User.objects.create_user(username='testuser', password='123456')
    fav = FavoriteMovie.objects.create(
        user=user,
        tmdb_id=550,
        title='Fight Club',
        poster_path='/pB8BM7pdSp6B6Ih7QZ4CPRiFj7.jpg'
    )
    assert fav.title == 'Fight Club'
    assert str(fav) == 'Fight Club'