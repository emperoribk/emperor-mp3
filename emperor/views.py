from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

# Create your views here.

def index(request):
    song = Song.objects.all()
    return render(request, 'index.html', {'song':song})

def song(request):
    song = Song.objects.all()
    return render(request,'song.html', {'song':song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request,'songpost.html', {'song':song})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')