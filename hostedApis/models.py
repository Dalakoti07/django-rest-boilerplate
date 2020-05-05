from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class SongCategory(models.Model):
    name = models.CharField(max_length=20)
    categoryPicture = models.ImageField(upload_to='categories')

class EachSong(models.Model):
    category = models.CharField(max_length=20,default='')
    name = models.CharField(max_length=20)
    songUrl = models.CharField(max_length=200)
    artist = models.CharField(max_length=20)