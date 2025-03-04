# music/views.py
from django.http import HttpResponse
from django.shortcuts import render

# Пример функции представления
def home(request):
     return render(request, 'music/home.html') 

# Другие представления
def search(request):
    return HttpResponse("Search Page")

def group_detail(request, group_id):
    return HttpResponse(f"Group {group_id} details")

def album_detail(request, album_id):
    return HttpResponse(f"Album {album_id} details")

def song_detail(request, song_id):
    return HttpResponse(f"Song {song_id} details")
