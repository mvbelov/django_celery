import datetime
import time

import channels.layers
import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from django.contrib.auth.models import User

from django_celery.celery import app

channel_layer = channels.layers.get_channel_layer()


@app.task()
def summ():
    user = User.objects.all()
    print(user[0].username, 'Результат сложения')
    return user[0].username


@shared_task
def send_to_chat():
    date = datetime.datetime.now()
    async_to_sync(channel_layer.group_send)(
        'chat_pupsiki', {
            'type': 'send_timer',
            'time': str(date)
        })
    send_euro.apply_async(countdown=2)


@shared_task
def send_euro():
    euro = requests.get(f'https://www.nbrb.by/api/exrates/rates/431').json()
    async_to_sync(channel_layer.group_send)(
        'chat_pupsiki', {'type': 'send_kurs', 'kurs': str(euro)}
    )
