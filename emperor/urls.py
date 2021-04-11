from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('song', views.song, name='song'),
    path('song/<int:id>', views.songpost, name='songpost'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
]