from django.db import models

# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    artiste = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    image = models.FileField(upload_to = 'img')
    song = models.FileField(upload_to='song')
    

    def __str__(self):
        return self.name  +  'by' +  self.artiste
