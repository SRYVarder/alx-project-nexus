from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class FavouriteMovie(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='favourites')
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200, blank=True, null=True)   
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tmdb_id')

    def __str__(self):
        return self.title
