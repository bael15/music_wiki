from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    formed_date = models.DateField()  # это может быть поле для даты создания
    image = models.ImageField(upload_to='groups/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название альбома")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='albums', verbose_name="Группа")
    release_date = models.DateField(verbose_name="Дата выпуска")
    cover = models.ImageField(upload_to='album_covers/', blank=True, null=True, verbose_name="Обложка альбома")

    def __str__(self):
        return f"{self.title} - {self.group.name}"

class Song(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название песни")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True, related_name='songs', verbose_name="Альбом")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='songs', verbose_name="Группа")
    duration = models.DurationField(verbose_name="Длительность")
    audio_file = models.FileField(upload_to='songs/', verbose_name="Файл с песней")
    lyrics = models.TextField(blank=True, null=True, verbose_name="Текст песни")

    def __str__(self):
        return self.title

class GroupMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    biography = models.TextField(blank=True, null=True, verbose_name="Биография")
    role = models.CharField(max_length=100, verbose_name="Роль")
    birth_date = models.DateField(verbose_name="Дата рождения")
    photo = models.ImageField(upload_to='members_photos/', blank=True, null=True, verbose_name="Фотография")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members', verbose_name="Группа")

    def __str__(self):
        return f"{self.name} ({self.role})"
