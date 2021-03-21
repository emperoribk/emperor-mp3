from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('song', views.song, name='song'),
    path('song/<int:id>', views.songpost, name='songpost')
]