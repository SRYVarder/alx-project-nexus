from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    overview = serializers.CharField()
    genre = serializers.CharField(max_length=100)
    release_date = serializers.DateField()
    poster_path = serializers.CharField(max_length=200, allow_null=True)
    vote_average = serializers.FloatField()

class FavouriteMovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tmdb_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    poster_path = serializers.CharField(max_length=200, allow_null=True)
    added_at = serializers.DateTimeField(read_only=True)

