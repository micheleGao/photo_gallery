from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Artist, Gallery, Review

class GallerySerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail', 
        read_only=True
    )
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset= Artist.objects.all(),
        source = 'artist'
    )
    class Meta:
        model = Gallery
        fields = ('id', 'artist', 'artist_id', 'title', 'art_url')
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail', read_only=True)

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(), source='artist')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'artist', 'title','artist_id',
                  'body', 'created', 'owner')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    gallery= GallerySerializer(
        many= True,
        read_only = True
    )
    reviews=ReviewSerializer(
        many=True, 
        read_only =True
    )
    artist_url=serializers.ModelSerializer.serializer_url_field(view_name='artist_detail')
    class Meta:
        model = Artist
        fields = ('id', 'photo_url','artist_url', 'nationality', 'name','reviews', 'gallery')


