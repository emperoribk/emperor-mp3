from emperor.forms import PostForm
from django.db.models import query_utils
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Song
from django.contrib import messages
from django.views.generic import CreateView


def search(request):
    query = request.GET.get('query')
    song = Song.objects.all()
    qs = song.filter(name__icontains=query)
    return render(request, 'search.html', {'songs':qs, 'query':query})

def index(request):
    query = "Afro beats"
    songs = Song.objects.filter(tag=query)
    Gospel = "Gospel"
    gospel = Song.objects.filter(tag=Gospel)
    Hiphop = "Hip hop"
    hiphop = Song.objects.filter(tag=Hiphop)
    song = Song.objects.all()
    return render(request, 'index.html', {'song':song, "songs":songs, 'gospel':gospel, 'hiphop':hiphop})

def song(request):
    song = Song.objects.all()
    return render(request,'song.html', {'song':song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request,'songpost.html', {'song':song})

def afro(request):
    query = "Afro beats"
    song = Song.objects.filter(tag=query)
    return render(request, 'afro.html', {"songs":song})

def gospel(request):
    query = "Gospel"
    gospel = Song.objects.filter(tag=query)
    return render(request, 'gospel.html', {'gospel':gospel})

def hiphop(request):
    query = "Hip hop"
    hiphop = Song.objects.filter(tag=query)
    return render(request, 'hiphop.html',{'hiphop':hiphop})

class PostCreateView(CreateView):
    template_name = 'upload.html'
    form_class = PostForm
    queryset = Song.objects.all()
    success_url = '/'
    


