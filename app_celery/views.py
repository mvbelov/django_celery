from django.shortcuts import render

from django_celery.tasks import summ


def get_page(request):
    summ.delay()
    return render(request, 'index.html')

def get_wind(request):
    return render(request, 'chat.html')

def get_room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
