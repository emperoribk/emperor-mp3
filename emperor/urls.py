from django.urls import path,include
from . import views
from .views import PostCreateView


urlpatterns = [
    path('', views.index, name='index'),
    path('song', views.song, name='song'),
    path('song/<int:id>', views.songpost, name='songpost'),
    path('afro/', views.afro),
    path('gospel/',views.gospel),
    path('hiphop/',views.hiphop),
    path('search/', views.search),
    path('upload/', PostCreateView.as_view())
    
]