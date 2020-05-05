from django.contrib import admin

# Register your models here.
from .models import Hero,SongCategory,EachSong

admin.site.register([Hero,SongCategory,EachSong])