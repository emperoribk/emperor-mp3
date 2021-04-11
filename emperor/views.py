from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CreateUserForm


def index(request):
    song = Song.objects.all()
    return render(request, 'index.html', {'song':song})

def song(request):
    song = Song.objects.all()
    return render(request,'song.html', {'song':song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request,'songpost.html', {'song':song})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        
        myuser.save()
        user_self = request.POST['username']
        messages.success(request,'Account has been successfully created by ' + user_self)

        return redirect('/signin')

    return render(request, 'signup.html')

