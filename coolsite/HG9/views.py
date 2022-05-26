# Импорт функций и пакетов
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Определение списка меню как словаря
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]

# Функция представления для главной страницы
def index(request):
    posts = Product.objects.all()

# Словарь с перечисленными параметрами
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    # Путь к шаблону главной страницы
    return render(request, 'HG9/index.html', context=context)

# Функция представления для страницы о сайте
def about(request):
    return render(request, 'HG9/about.html', {'menu': menu, 'title': 'О сайте'})

# Функция представления для страницы с добавлением статей
def addpage(request):
    return HttpResponse("Добавление статьи")

# Функция представления для страницы с обратной связью
def contact(request):
    return HttpResponse("Обратная связь")

# Функция представления для страницы авторизации
def login(request):
    return HttpResponse("Авторизация")

# Функция представления для страницы статей
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


# Функция отображения по рубрикам
def show_category(request, cat_id):
    posts = Product.objects.filter(cat_id=cat_id)

    # Если количество постов = 0, то генерируем ошибку (Заготовка)
    if len(posts) == 0:
        raise Http404()

    # Словарь с перечисленными параметрами
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    # Путь к шаблону отображения по рубрикам
    return render(request, 'HG9/index.html', context=context)