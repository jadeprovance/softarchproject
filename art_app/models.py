# models.py in art_app

from django.contrib.auth.models import User
from django.db import models

class ArtPiece(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField()
    description = models.TextField()
    artist = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    art_piece = models.ForeignKey(ArtPiece, on_delete=models.CASCADE)
    text = models.TextField()

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    art_piece = models.ForeignKey(ArtPiece, on_delete=models.CASCADE)
