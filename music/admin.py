from django.contrib import admin
from .models import Group, Album, Song, GroupMember

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'formed_date')
    search_fields = ('name',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'release_date')
    search_fields = ('title', 'group__name')
    list_filter = ('release_date',)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'album', 'duration')
    search_fields = ('title', 'group__name', 'album__title')
    list_filter = ('album',)

@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'group')
    search_fields = ('name', 'group__name')
