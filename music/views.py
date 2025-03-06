from django.shortcuts import render
from .models import Group, Album, Song  

def home(request):
    groups = Group.objects.all().order_by('-created_at')[:5]  # последние 5 групп
    albums = Album.objects.all().order_by('-created_at')[:5]  # последние 5 альбомов
    songs = Song.objects.all().order_by('-created_at')[:5]  # последние 5 песен

    return render(request, 'music/home.html', {'groups': groups, 'albums': albums, 'songs': songs})

def search(request):
    query = request.GET.get('query', '')
    
    # Поиск по группам, альбомам и песням
    groups = Group.objects.filter(name__icontains=query)
    albums = Album.objects.filter(title__icontains=query)
    songs = Song.objects.filter(title__icontains=query)
    
    return render(request, 'music/search_results.html', {'query': query, 'groups': groups, 'albums': albums, 'songs': songs})

def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    albums = group.albums.all()  
    songs = Song.objects.filter(group=group)  # песни, относящиеся к группе
    return render(request, 'music/group_detail.html', {'group': group, 'albums': albums, 'songs': songs})


def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'music/song_detail.html', {'song': song})


def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    songs = album.songs.all() 
    return render(request, 'music/album_detail.html', {'album': album, 'songs': songs})
