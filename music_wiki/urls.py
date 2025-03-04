from django.contrib import admin
from django.urls import path, include  # Импортируем include для подключения URL-адресов приложений

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music.urls')),  # Исправлено с 'bai_music.urls' на 'music.urls'
]

