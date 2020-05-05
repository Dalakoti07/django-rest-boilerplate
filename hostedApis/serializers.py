from rest_framework import serializers

from .models import Hero,SongCategory,EachSong

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class SongCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SongCategory
        fields =('name','categoryPicture')

class EachSongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EachSong
        fields =('name','songUrl','artist')