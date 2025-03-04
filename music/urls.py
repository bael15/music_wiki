from django.urls import path
from . import views  # Импортируем представления из views.py

urlpatterns = [
    path('home/', views.home, name='home'),  # Путь для /home
    path('search/', views.search, name='search'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
]


