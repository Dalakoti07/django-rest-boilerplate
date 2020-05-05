from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer,SongCategorySerializer,EachSongSerializer
from .models import Hero,SongCategory,EachSong


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= SongCategory.objects.all().order_by('name')
    serializer_class = SongCategorySerializer

class EachSongViewSet(viewsets.ModelViewSet):
    queryset = EachSong.objects.all().order_by('name')
    serializer_class = EachSongSerializer

class GetSongOfCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = EachSongSerializer
    def get_queryset(self):
        categoryRequested = self.request.query_params.get('category')
        print("requested category is ",categoryRequested)
        if categoryRequested != None:
            queryset = EachSong.objects.all().filter(category=categoryRequested)
        else:
            queryset = EachSong.objects.all().filter(category="none")
        return queryset