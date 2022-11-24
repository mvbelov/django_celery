import time

from django.contrib.auth.models import User

from django_celery.celery import app


@app.task()
def summ():
    user = User.objects.all()
    print(user[0].username, 'Результат сложения')
    return user[0].username
