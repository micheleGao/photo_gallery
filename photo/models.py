from django.db import models


# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()
    def __str__(self):
        return self.name
class Gallery(models.Model) :
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='gallery')
    title = models.CharField(max_length=100, default='no title')
    art_url = models.CharField(max_length=200, null=True)

    def __str__(self):
      return self.title

class Review(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'users.User', related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.title