from django.db import models
from musician.models import Musician
# Create your models here.

class Album(models.Model):
   album_name=models.CharField(max_length=100)
   musician_name=models.ForeignKey(Musician, on_delete=models.CASCADE)
   album_release_date=models.DateField()
   album_rating = models.IntegerField(default=0, choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ])
   
   def __str__(self):
      return self.album_name
   