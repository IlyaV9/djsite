from django.http import HttpResponse
from django.shortcuts import render

from .models import *

menu = ["О сайте", "Продукты", "Обратная связь", "Войти"]

def index(reqvest):
    posts = Product.objects.all()
    return render(reqvest, 'HG9/index.html', {'posts':posts, 'menu': menu, 'title': 'Главная страница'})

def about(reqvest):
    return render(reqvest, 'HG9/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(reqvest, catid):
    return HttpResponse(f"<h1>Продукция</h1><p>{catid}</p>")

def archive(reqvest, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

