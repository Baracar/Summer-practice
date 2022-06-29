import random
from django.http import HttpResponse
import time


def index(request):
    time.sleep(random.randint(100, 5000)/1000)
    return HttpResponse("<h2>Главная</h2>")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")