# Импорт функций и пакетов
from django.contrib import admin
from .models import *

# Класс для админ панели (список полей которые видим)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

# Класс для админ панели (список полей которые видим)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

# Регистрация моделей для админ панели
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
