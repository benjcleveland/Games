from django.db import models

# Create your models here.
class Game(models.Model):

    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    last_played = models.DateTimeField('last played')
    image_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)

class Rating(models.Model):
    
    def __unicode__(self):
        return self.rating

    game = models.ForeignKey(Game)
    rating = models.IntegerField()
