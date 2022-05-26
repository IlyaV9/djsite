# Импорт функций и пакетов
from django import template
from HG9.models import *

# Создаём экземпляр класса Library (регистрация собственных шаблонов тэгов)
register = template.Library()


@register.simple_tag(name='getcats') # Превращение функции в тэг
def get_categories(filter=None): # Функция для работы простого тэга
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('HG9/list_categories.html') # Превращение функции в тэг
def show_categories(sort=None, cat_selected=0): # Функция для работы простого тэга
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats":cats, "cat_selected": cat_selected}
