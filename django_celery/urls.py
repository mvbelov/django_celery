from django.contrib import admin
from django.urls import path

from app_celery.views import get_page, get_wind, get_room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_page, name='get_page'),
    path('chat/', get_wind),
    path('<str:room_name>/', get_room),
]
