from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    # Категория
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name ='Категория'
        verbose_name_plural = 'Категории'


# class Product(models.Model):
#     # Жанры
#     name = models.CharField("Имя", max_length=150)
#     description = models.TextField("Описание")
#     url = models.SlugField(max_length=160, unique=True)
#     image = models.ImageField("Изображение", upload_to="actors/")
#
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Product'
#         verbose_name_plural = 'Products'


class Movie(models.Model):
    # Фильмы
    title = models.CharField("Название", max_length=100)
    poster = models.ImageField("Постер", upload_to="products/")
    genres = models.IntegerField("Сумма")
    # genres = models.ManyToManyField(Product, verbose_name="жанры")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draf = models.BooleanField("Черновик", default=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug":self.url})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'



