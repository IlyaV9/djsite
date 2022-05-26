# Импорт функций и пакетов
from django.db import models
from django.urls import reverse

# Создание таблицы/модели/класса Product о товаре
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    price = models.IntegerField(default=0, verbose_name="Цена")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория") # Внешний ключ

    # Метод для вывода заголовков текущей записи (возврат имени продукта)
    def __str__(self):
        return self.title

    # Формирование маршрута для конкретной записи
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    # Вложенный класс Meta для настройки модели Product
    class Meta:
        verbose_name = 'Товары' # Настройка админ панели
        verbose_name_plural = 'Товары' # Настройка админ панели
        ordering = ['time_create', 'title'] # Порядок сортировки

# Создание таблицы/модели/класса Category о товаре
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    # Метод для вывода заголовков текущей записи (возврат имени категории)
    def __str__(self):
        return self.name

    # Формирование маршрута для конкретной категории
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    # Вложенный класс Meta для настройки модели Category
    class Meta:
        verbose_name = 'Категория' # Настройка админ панели
        verbose_name_plural = 'Категории' # Настройка админ панели
        ordering = ['id'] # Порядок сортировки
