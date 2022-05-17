from django.http import HttpResponse
from django.shortcuts import render

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]

def index(reqvest):
    posts = Product.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(reqvest, 'HG9/index.html', context=context)

def about(request):
    return render(request, 'HG9/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
