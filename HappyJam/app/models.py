"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Music(models.Model):
    music = models.TextField(null = True)

class Movie(models.Model):
    movie = models.TextField(null=True)
    music_id = models.ForeignKey(Music, on_delete=models.CASCADE, null = True)


class Instrument(models.Model):
    instrument = models.CharField(max_length=30)
    
    def __str__(self):
        return self.instrument



class User(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)


class Single(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE ,)
    instrument_id = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.uid
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["uid","instrument_id"],
                name = "single_unique"
            ),
        ]

class Room(models.Model):
    user = models.IntegerField()
    room_id = models.IntegerField(null=True)
    instrument_id = models.ForeignKey(Instrument, on_delete=models.CASCADE, null = True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.user
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["room_id","user"],
                name = "room_unique"
            ),
        ]